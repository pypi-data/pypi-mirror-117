#!/bin/bash

###############################################################################
# Bash script to install Azure Databricks cluster libraries.
# This script has a dependency on the 'Configure Databricks'
# task, which sets up the '$2' profile.
#
# Unlike the UI, the API cannot install a library across all clusters.
#
# Cluster Libraries are defined in /System/G2/Databricks/Libraries/dv-libraries.json
#
# example: ./install-libraries.sh in-libraries.json IN
#
# sample json:
#    "clusters": [
#        {
#            "cluster_name": "DataEngineering-Link",
#            "libraries": [
#                {
#                    "pypi": {
#                        "package": "snowflake-connector-python"
#                    }
#                }
#            ]
#        }
#   ]
###############################################################################

# Python 3 is required


# require args
if [[ $# -eq 0 ]] ; then
    echo 'Path to cluster JSON config was not provided!'
    exit 1
fi
if [ -z "$2" ]
then
    echo "Profile was not provided!"
fi

# first arg is the path to configuration
pathToConfig=$1

if [ ! -f "$pathToConfig" ]; then
    echo "$pathToConfig does not exist!"
    exit 1
fi

echo "======================= Install Databricks Clusters Libraries ======================="

echo "    ==> reading ${pathToConfig}"
raw_json=`cat ${pathToConfig}`

# get list of clusters, filter on name
echo "    ==> getting databricks clusters..."
existing_clusters=`databricks clusters list --profile $2 --output JSON | jq -c '. // empty'`

stopped_clusters=()

# get cluster libraries
for row in $(echo "${raw_json}" | jq -r '.clusters[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    
    cluster=$(_jq '.')
    
    # get cluster name for lookup
    cluster_name=$(_jq '.cluster_name')
    echo "    ==> starting cluster [${cluster_name}]..."
    existing_cluster=`echo "${existing_clusters}" | jq -r '[.clusters[]?|select( .cluster_name == "'${cluster_name}'")][0] // empty'`
    # if cluster exists with name, update it. otherwise create it.
    if [ -z "$existing_cluster" ]
    then
        echo "    ==> FATAL ERROR: could not find cluster [${cluster_name}]!" 1>&2
        exit 500
    else
        cluster_id=`echo "${existing_cluster}" | jq -r '.cluster_id'`
        cluster_state=`echo "${existing_cluster}" | jq -r '.state'`
        
        echo "    ==> cluster [${cluster_id}] found in [${cluster_state}] state..."
        echo "    ==> getting libraries cluster-status for [${cluster_name}]..."
        
        installed_libraries=`databricks libraries cluster-status --cluster-id ${cluster_id} --profile $2 | jq -c '. // empty'`
        echo "    ==> ${installed_libraries}"
        
        # pypi package start =========================================================================
        pypi_packages=`echo "${cluster}" | jq -r '[.libraries[].pypi| select(.)] // empty'`
        #echo "    ==> ${pypi_packages}"
        for pypi_package in $(echo "${pypi_packages}" | jq -r '.[] | @base64'); do
            _jq2() {
                echo ${pypi_package} | base64 --decode | jq -r ${1}
            }
            package=$(_jq2 '.package')
            
            echo "    ==> checking cluster [${cluster_name}] for pypi package [${package}]..."
            library_status=`echo "${installed_libraries}" | jq -r '.library_statuses[]? | select(.library.pypi.package == "'${package}'") | .status // empty'`
            #echo "{$library_status}"
            echo "    ==> pypi package [${package}] status is [${library_status}]..."
            
            if [[ "${library_status}" != "INSTALLED" && "${library_status}" != "INSTALLING" && "${library_status}" != "PENDING" ]]; then
                echo "    ==> pypi package [${package}] missing from cluster [${cluster_name}]..."
                
                # cluster must be running before installing
                if [ "${cluster_state}" == "TERMINATED" ]; then
                    stopped_clusters+=(${cluster_id})
                    echo "    ==> cluster [${cluster_name}] (${cluster_id}) not running, sending startup command..."
                    databricks clusters start --cluster-id "${cluster_id}" --profile $2
                    # just start for now, install in next loop to provide time to startup and
                    # issue start command to parallel cluster startup
                    
                else
                    echo "    ==> installing pypi package [${package}]..."
                    databricks libraries install --cluster-id "${cluster_id}" --pypi-package "${package}" --profile $2
                    if [ $? -eq 0 ]; then
                        echo "    ==> installed pypi package [${package}]!"
                    else
                        echo "    ==> FATAL ERROR: could not install pypi package [${package}]!" 1>&2
                        exit 500
                    fi
                fi
            else
                echo "    ==> pypi package [${package}] already installed!"
            fi
        done
        # pypi package end =========================================================================
        
    fi
    
done
echo "    ==> "
echo "    ==> ===================  Initial cold-cluster check complete =================="
echo "    ==> "
existing_clusters=`databricks clusters list --profile $2 --output JSON | jq -c '. // empty'`

# now install for clusters that were terminated
for row in $(echo "${raw_json}" | jq -r '.clusters[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    
    cluster=$(_jq '.')
    
    # get cluster name for lookup
    cluster_name=$(_jq '.cluster_name')
    
    cluster_id=`echo "${existing_cluster}" | jq -r '.cluster_id'`
    cluster_state=`echo "${existing_cluster}" | jq -r '.state'`
    
    echo "    ==> cluster [${cluster_id}] found in [${cluster_state}] state..."
    echo "    ==> getting libraries cluster-status for [${cluster_name}]..."
    
    installed_libraries=`databricks libraries cluster-status --cluster-id ${cluster_id} --profile $2 | jq -c '. // empty'`
    echo "    ==> ${installed_libraries}"
    
    # pypi package =========================================================================
    pypi_packages=`echo "${cluster}" | jq -r '[.libraries[].pypi| select(.)] // empty'`
    #echo "    ==> ${pypi_packages}"
    for pypi_package in $(echo "${pypi_packages}" | jq -r '.[] | @base64'); do
        _jq2() {
            echo ${pypi_package} | base64 --decode | jq -r ${1}
        }
        package=$(_jq2 '.package')
        
        echo "    ==> checking cluster [${cluster_name}] for pypi package [${package}]..."
        library_status=`echo "${installed_libraries}" | jq -r '.library_statuses[]? | select(.library.pypi.package == "'${package}'") | .status // empty'`
        #echo "{$library_status}"
        echo "    ==> pypi package [${package}] status is [${library_status}]..."
        
        if [[ "${library_status}" != "INSTALLED" && "${library_status}" != "INSTALLING" && "${library_status}" != "PENDING" ]]; then
            echo "    ==> pypi package [${package}] missing from cluster [${cluster_name}]..."
            
            attempt_counter=0
            max_attempts=10
            new_cluster_state=`databricks clusters get --cluster-id "${cluster_id}" --profile $2 | jq -r '.state'`
            
            # wait for cluster to start
            # cluster must be running before installing
            while [ "${new_cluster_state}" != "RUNNING" ]
            do
                
                echo "        ==> waiting for cluster [${cluster_name}] to start..."
                if [ ${attempt_counter} -eq ${max_attempts} ];then
                    echo "    ==> FATAL ERROR: max attempts reached for starting cluster!" 1>&2
                    exit 500
                fi
                
                new_cluster_state=`databricks clusters get --cluster-id "${cluster_id}" --profile $2 | jq -r '.state'`
                echo "        ==> current state of cluster [${cluster_name}] is [${new_cluster_state}]..."
                if [ "${new_cluster_state}" == "RUNNING" ]; then
                    break
                fi
                attempt_counter=$(($attempt_counter+1))
                echo "        ==> sleeping 60s before polling again for state..."
                sleep 60
            done
            
            
            echo "    ==> installing pypi package [${package}]..."
            databricks libraries install --cluster-id "${cluster_id}" --pypi-package "${package}" --profile $2
            if [ $? -eq 0 ]; then
                echo "    ==> installed pypi package [${package}]!"
            else
                echo "    ==> FATAL ERROR: could not install pypi package [${package}]!" 1>&2
                exit 500
            fi
            
        else
            echo "    ==> pypi package [${package}] already installed!"
        fi
    done
    
done

# now stop clusters that were stopped before we attempted to install
for stopped_cluster_id in ${stopped_clusters[@]}; do
    
    echo "    ==> stopping cluster (${stopped_cluster_id}) because it was stopped when script started..."
    databricks clusters delete --cluster-id "${stopped_cluster_id}" --profile $2
    
done

echo "============== Completed Installing Databricks Clusters Libraries ======================="