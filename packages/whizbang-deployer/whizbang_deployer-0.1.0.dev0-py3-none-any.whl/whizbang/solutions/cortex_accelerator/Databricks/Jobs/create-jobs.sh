#!/bin/bash

###############################################################################
# Bash script to create Azure Databricks jobs.
# This script has a dependency on the 'Configure Databricks'
# task, which sets up the 'AZDO' profile.
#
# Jobs are defined in /System/G2/Databricks/Jobs/dv-jobs.json
#
# example: ./create-jobs.sh dv-jobs.json IN northcentralus.azuredatabricks.net <personal-access-token>
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

echo "======================= Create Databricks Jobs ======================="

# Get existing jobs
echo "    ==> getting databricks jobs..."
existing_jobs=`databricks jobs list --profile $2 --output JSON | jq -c '[.jobs[]? | {job_name: .settings.name, job_id: .job_id}] // empty'`
if [ $? -ne 0 ]; then
    echo "    ==> FATAL ERROR: Databricks CLI 'databricks jobs list' failed! Cannot continue." 1>&2
    exit 500
fi

echo "    ==> reading ${path_to_config}"
raw_json=`cat ${path_to_config}`


# Loop through each item in json collection and create using the databricks cli
for row in $(echo "$raw_json" | jq -r '.jobs[] | @base64'); do
    _jq() {
        echo "$row" | base64 --decode | jq -r ${1}
    }
    
    new_job=`echo "$(_jq '.settings')" | jq -c '.'`
    new_grants=`echo "$(_jq '.grants')" | jq -c '.'`
    
    # get job name for lookup
    job_name=$(_jq '.settings.name')
    echo "    ==> processing [$job_name]..."
    
    # get job id if it exists
    jqfilter='[.[]|select( .job_name == "'${job_name}'")][0] // empty | .job_id'
    job_id=`echo "${existing_jobs}" | jq -r "${jqfilter}"`
    
    # get existing cluster by name
    cluster_name=$(_jq '.settings.existing_cluster_name')
    
    if [ "${cluster_name}" = "null" ]
    then
        echo "    ==> skipping existing cluster check..."
    else
        echo "    ==> checking for databricks cluster [$cluster_name]..."
        existing_cluster=`databricks clusters list --profile $2 --output JSON | jq -r '[.clusters[]?|select( .cluster_name == "'${cluster_name}'")][0] // empty'`
        
        # fail if cluster not found.
        if [ -z "$existing_cluster" ]
        then
            echo "    ==> FATAL ERROR: cluster [$cluster_name] not found! Cannot continue." 1>&2
            exit 500
        fi
        
        cluster_id=`echo "${existing_cluster}" | jq -r '.cluster_id'`
        echo "    ==> cluster [${cluster_name}] found with id [${cluster_id}]..."
        
        # inject cluster id into json
        echo "    ==> using cluster [${cluster_name}] found with id [${cluster_id}]..."
        new_job=`echo "${new_job}" | jq --arg cluster_id ${cluster_id} '. + {"existing_cluster_id": $cluster_id}' | jq -c '.'`
    fi
    
    
    # if job exists with name, get id, otherwise create it.
    if [ -z "$job_id" ]
    then
        
        #create new job
        echo "    ==> job [${job_name}] not found, creating new job..."
        
        new_job_id=`databricks jobs create --json """${new_job}""" --profile $2 | jq -r '.job_id // empty'`
        if [ $? -ne 0 ]; then
            echo "    ==> FATAL ERROR: Databricks CLI 'databricks jobs create' failed! Cannot continue." 1>&2
            exit 500
        fi
        echo "    ==> created job [${job_name}] id [${new_job_id}]."
        
        # inject new job into existing jobs json (to prevent dupes in the same run)
        new_job=`echo "${new_job}" | jq --arg id ${new_job_id} '. + {"job_id": $id}' | jq -c .`
        existing_jobs=`echo "${existing_jobs}" | jq '. += ['"${new_job}"']' | jq -c .`
        job_id=${new_job_id}
    else
        
        #reset (update) existing job
        echo "    ==> job [${job_name}] found with id [${job_id}], resetting existing job..."
        databricks jobs reset --job-id ${job_id} --json "${new_job}" --profile $2
        if [ $? -ne 0 ]; then
            echo "    ==> FATAL ERROR: Databricks CLI 'databricks jobs reset' failed! Cannot continue." 1>&2
            exit 500
        fi
        echo "    ==> reset job [${job_name}] with id [${job_id}]."
    fi
    
    new_grants_count=`echo "$(_jq '.grants')" | jq -c 'length'`
    echo "    ==> [${new_grants_count}] grants defined in json config..."
    if [ "${new_grants_count}" -eq 0 ]
    then
        echo "    ==> grants not defined in json config, skipping grants..."
    else
        echo "    ==> setting grants for [$job_name] (${job_id})..."
        echo "    ==> new grants: ${new_grants}"
        echo "    ==> getting existing grants..."
        existing_grants=`curl -s -H "Authorization: Bearer ${pat}" -H "Content-Type: application/json" -X GET "https://${databricks_instance}/api/2.0/jobs/get?job_id=${job_id}&include_acls=true" | jq -c '{job_id: '${job_id}', grants: [.grants[]?  | select(.permission != "MANAGE") | { user_id, permission}]}'`
        existing_grants_count=`echo "${existing_grants}" | jq -c 'length'`
        echo "    ==> [${existing_grants_count}] existing grants: ${existing_grants}"
        
        all_grants=`echo ${existing_grants} | jq -c '.grants += '${new_grants}''`
        final_grants=`echo ${all_grants} | jq -c '{job_id, grants: .grants | unique }'`
        final_grants_count=`echo "${final_grants}" | jq -c '.grants | length'`
        echo "    ==> [${final_grants_count}] final grants: ${final_grants}"
        
        if [ "${final_grants_count}" -eq 0 ]
        then
            echo "    ==> FATAL ERROR: zero grants, job must have an IS_OWNER! Cannot continue." 1>&2
            exit 500
        fi
        grants_has_owner=`echo "${final_grants}" | jq -c '[.grants[] | select(.permission == "IS_OWNER")] | length'`
        
        if [ "${grants_has_owner}" -ne 1 ]
        then
            echo "    ==> FATAL ERROR: Job must have exactly one IS_OWNER! Cannot continue." 1>&2
            exit 500
        fi
        
        curl -s -H "Authorization: Bearer ${pat}" -H "Content-Type: application/json" -X POST "https://${databricks_instance}/api/2.0/jobs/reset-acl"  -d ${final_grants}
        if [ $? -ne 0 ]; then
            echo "    ==> FATAL ERROR: Failed calling 'https://${databricks_instance}/api/2.0/jobs/reset-acl'! Cannot continue." 1>&2
            exit 500
        fi
    fi
    echo "    ==> finished [$job_name]!"
    echo "====================================================================="
    
done

echo "============== Completed Create Databricks Jobs ======================="