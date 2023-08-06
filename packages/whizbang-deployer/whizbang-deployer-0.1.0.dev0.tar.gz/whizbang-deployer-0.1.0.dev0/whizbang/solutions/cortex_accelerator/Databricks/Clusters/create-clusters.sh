#!/bin/bash

###############################################################################
# Bash script to create Azure Databricks clusters.
# This script has a dependency on the 'Configure Databricks'
# task, which sets up the 'AZDO' profile.
#
# Clusters are defined in /System/G2/Databricks/Clusters/dv-clusters.json
#
###############################################################################

# Python 3 is required


# require
if [[ $# -eq 0 ]] ; then
    echo 'Path to cluster JSON config was not provided!'
    exit 1
fi

# first arg is the env abbreviation
pathToConfig=$1

if [ ! -f "$pathToConfig" ]; then
    echo "$pathToConfig does not exist!"
    exit 1
fi

echo "======================= Create Databricks Pools & Clusters ======================="

echo "    ==> getting databricks instance-pools..."

# Get all instance_pools
existing_instance_pools=`databricks instance-pools list --profile AZDO --output JSON | jq -c '[.instance_pools[]? | {instance_pool_name: .instance_pool_name, instance_pool_id: .instance_pool_id}] // empty'`

echo "    ==> reading ${pathToConfig}"
raw_json=`cat ${pathToConfig}`

# Loop through each instance_pool in json collection and create using the databricks cli
for row in $(echo "${raw_json}" | jq -r '.instance_pools[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    
    instance_pool=$(_jq '.')
    
    # get instance_pools name for lookup
    instance_pool_name=$(_jq '.instance_pool_name')
    echo "    ==> processing [$instance_pool_name]..."
    
    # get instance_pool id if it exists
    instance_pool_id=`echo ${existing_instance_pools} | jq -r '[.[]|select( .instance_pool_name == "'${instance_pool_name}'")][0] // empty | .instance_pool_id'`
    
    # if instance_pool exists with name, get id, otherwise create it.
    if [ -z "$instance_pool_id" ]
    then
        echo "    ==> instance_pool [${instance_pool_name}] not found, creating new instance_pool..."
        echo "    ==> ${instance_pool}"
        new_instance_pool=`databricks instance-pools create --json "${instance_pool}" --profile AZDO`
        new_instance_pool=`echo ${new_instance_pool} | jq --arg name ${instance_pool_name} '. + {"instance_pool_name": $name}' | jq -c .`
        existing_instance_pools=`echo ${existing_instance_pools} | jq '. += ['${new_instance_pool}']' | jq -c .`
    else
        echo "    ==> instance_pool [${instance_pool_name}] found with id [${instance_pool_id}], updating existing instance_pool..."
        instance_pool=`echo "${instance_pool}" | jq --arg id ${instance_pool_id} '. + {"instance_pool_id": $id}' | jq -c .`
        echo "    ==> ${instance_pool}"
        databricks instance-pools edit --json "${instance_pool}" --profile AZDO
    fi
    
    echo "    ==> finished [$instance_pool_name]! "
    echo "====================================================================="
    
done


# Loop through each cluster in json collection and create using the databricks cli
for row in $(echo "${raw_json}" | jq -r '.clusters[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    
    cluster=$(_jq '.')
    
    # get cluster name for lookup
    cluster_name=$(_jq '.cluster_name')
    echo "    ==> processing cluster [${cluster_name}]..."
    
    # get instance_pool_name for lookup
    cluster_instance_pool_name=`echo "${cluster}" | jq -r '.instance_pool_name // empty'`
    
    # lookup instance pool name, map to id
    if [ -n "$cluster_instance_pool_name" ]
    then
        echo "    ==> cluster configured to use instance_pool, mapping to instance_pool_id..."
        cluster_instance_pool_id=`echo ${existing_instance_pools} | jq -r '[.[]|select( .instance_pool_name == "'${cluster_instance_pool_name}'")][0] // empty | .instance_pool_id'`
        if [ -z "$cluster_instance_pool_id" ]
        then
            echo "    ==> FATAL ERROR: instance_pool [${cluster_instance_pool_name}] missing!" 1>&2
            exit 500
        fi
        
        echo "    ==> cluster mapped to use instance_pool id [${cluster_instance_pool_id}]..."
        cluster=`echo "${cluster}" | jq --arg id ${cluster_instance_pool_id} '. + {"instance_pool_id": $id}' | jq -c .`
    fi
    
    echo "    ==> getting databricks clusters..."
    # get list of clusters, filter on name
    existing_cluster=`databricks clusters list --profile AZDO --output JSON | jq -r '[.clusters[]?|select( .cluster_name == "'${cluster_name}'")][0] // empty'`
    
    # if cluster exists with name, update it. otherwise create it.
    if [ -z "$existing_cluster" ]
    then
        echo "    ==> cluster not found, creating new cluster [${cluster_name}]..."
        #echo "    ==> ${cluster}"
        databricks clusters create --json "${cluster}" --profile AZDO
        if [ $? -eq 0 ]; then
            echo "    ==> created [${cluster_name}]!"
        else
            echo "    ==> FATAL ERROR: could not create [${cluster_name}]!" 1>&2
            exit 500
        fi
        
    else
        cluster_id=`echo "${existing_cluster}" | jq -r '.cluster_id'`
        echo "    ==> cluster [${cluster_id}] found, updating existing cluster..."
        cluster=`echo "${cluster}" | jq --arg id ${cluster_id} '. + {"cluster_id": $id}' | jq -c .`
        #echo "    ==> ${cluster}"
        databricks clusters edit --json "${cluster}" --profile AZDO
        if [ $? -eq 0 ]; then
            echo "    ==> edited [${cluster_name}]!"
        else
            echo "    ==> FATAL ERROR: could not edit [${cluster_name}]!" 1>&2
            exit 500
        fi
    fi
    
    
    echo "    ==> finished [$cluster_name]!"
    echo "====================================================================="
    
done
echo "============== Completed Create Databricks Pools & Clusters ======================="