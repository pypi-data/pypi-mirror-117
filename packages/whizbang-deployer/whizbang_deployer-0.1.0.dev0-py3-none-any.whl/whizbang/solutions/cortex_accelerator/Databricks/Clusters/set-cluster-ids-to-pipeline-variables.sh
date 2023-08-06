#!/bin/bash

###############################################################################
# Bash script to query Azure Databricks clusters and create pipeline variables.
# This script has a dependency on the 'Configure Databricks' task, which sets 
# up the 'AZDO' profile.
# 
# 
###############################################################################

# Python 3 is required
echo "======================= Set Databricks Cluster Ids ======================="

echo '    ==> getting clusters...'
raw_json=`databricks clusters list --profile AZDO --output JSON` 

echo '    ==> parsing clusters...'
existing_clusters=`echo "${raw_json}" | jq '[.clusters[]? | {cluster_id: .cluster_id, cluster_name: .cluster_name}] // empty'`

# Loop through each cluster in json collection and create using the databricks cli
for row in $(echo "${existing_clusters}" | jq -r '.[] | @base64'); do
    _jq() {
     echo ${row} | base64 -di | jq -r ${1}
    }
    cluster=$(_jq '.')

    # get cluster name & id for lookup
    cluster_name=$(_jq '.cluster_name')
    cluster_id=$(_jq '.cluster_id')

    echo "    ==> setting pipeline variable for cluster [${cluster_name}] to [${cluster_id}]..."
    cluster_name=`echo ${cluster_name^^}`
    cluster_name=`echo ${cluster_name//-}`
    
    echo '##vso[task.setvariable variable=CLUSTERLOOKUP_'$cluster_name';]'$cluster_id

done
echo "============== Completed Set Databricks Cluster Ids ======================="