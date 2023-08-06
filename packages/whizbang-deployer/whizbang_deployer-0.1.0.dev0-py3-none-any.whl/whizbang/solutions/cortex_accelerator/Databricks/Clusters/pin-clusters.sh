#!/bin/bash

###############################################################################
# Bash script to pin Azure Databricks clusters.
# This script has a dependency on the 'Configure Databricks'
# task, which sets up the '$2' profile.
#
#
# Clusters are defined in /System/G2/Databricks/Clusters/dv-clusters.json
#
# example: ./pin-clusters.sh in-clusters.json IN northcentralus.azuredatabricks.net <personal-access-token>
#
###############################################################################

# Python 3 is required


# require args
if [[ $# -ne 4 ]] ; then
    echo 'Missing command line arguments!'
    exit 1
fi

# first arg is the path to configuration
path_to_config=$1
databricks_instance=$3
pat=$4

if [ ! -f "$path_to_config" ]; then
    echo "$path_to_config does not exist!"
    exit 1
fi

echo "======================= Pin Databricks Clusters ======================="

echo "    ==> reading ${path_to_config}"
raw_json=`cat ${path_to_config}`

# get list of clusters, filter on name
echo "    ==> getting databricks clusters..."
existing_clusters=`databricks clusters list --profile $2 --output JSON | jq -c '. // empty'`

# Loop through each cluster in json collection 
for row in $(echo "${raw_json}" | jq -r '.clusters[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -r ${1}
    }
    
    cluster=$(_jq '.')
    
    # get cluster name for lookup
    cluster_name=$(_jq '.cluster_name')
    echo "    ==> processing cluster [${cluster_name}]..."
    existing_cluster=`echo "${existing_clusters}" | jq -r '[.clusters[]?|select( .cluster_name == "'${cluster_name}'")][0] // empty'`
    # if cluster exists with name, update it. otherwise create it.
    if [ -z "$existing_cluster" ]
    then
        echo "    ==> FATAL ERROR: could not find cluster [${cluster_name}]!" 1>&2
        exit 500
    else
        cluster_id=`echo "${existing_cluster}" | jq -r '.cluster_id'`
        cluster_state=`echo "${existing_cluster}" | jq -r '.state'`
        echo "    ==> cluster [$cluster_name] (${cluster_id}) found in [${cluster_state}] state..."
        echo "    ==> pinning cluster..."
        curl -n -s -H "Authorization: Bearer ${pat}" -H "Content-Type: application/json" -X POST https://${databricks_instance}/api/2.0/clusters/pin -d '{"cluster_id":"'${cluster_id}'"}' > /dev/null
    fi
    
    
    echo "    ==> finished [$cluster_name]!"
    echo "    ==> =================================================="
    
done
echo "============== Completed Pin Databricks Clusters ======================="