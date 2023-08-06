#!/bin/bash

###############################################################################
# Bash script to query Azure Databricks pools and create pipeline variables.
# This script has a dependency on the 'Configure Databricks' task, which sets 
# up the 'AZDO' profile.
# 
# 
###############################################################################

# Python 3 is required
echo "======================= Set Databricks Pool Ids ======================="

echo '    ==> getting pools...'
raw_json=`databricks instance-pools list --profile AZDO --output JSON` 

echo '    ==> parsing pools...'
existing_pools=`echo "${raw_json}" | jq '[.instance_pools[]? | {instance_pool_id: .instance_pool_id, instance_pool_name: .instance_pool_name}] // empty'`

# Loop through each pool in json collection and create using the databricks cli
for row in $(echo "${existing_pools}" | jq -r '.[] | @base64'); do
    _jq() {
     echo ${row} | base64 -di | jq -r ${1}
    }
    pool=$(_jq '.')

    # get pool name & id for lookup
    pool_name=$(_jq '.instance_pool_name')
    pool_id=$(_jq '.instance_pool_id')

    echo "    ==> setting pipeline variable for pool [${pool_name}] to [${pool_id}]..."
    pool_name=`echo ${pool_name^^}`
    pool_name=`echo ${pool_name//-}`
    
    echo '##vso[task.setvariable variable=POOLLOOKUP_'$pool_name';]'$pool_id

done
echo "============== Completed Set Databricks Pool Ids ======================="