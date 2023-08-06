#!/bin/bash

###############################################################################
# Bash script to install Azure Databricks cluster libraries.
# This script has a dependency on the 'Configure Databricks'
# task, which sets up the '$2' profile.
#
#
# Clusters are defined in /System/G2/Databricks/Clusters/dv-clusters.json
#
# example: ./install-libraries-all.sh in-clusters.json IN northcentralus.azuredatabricks.net <personal-access-token>
#
#
# sample json:
#    "all_clusters_libraries": [
#        {
#            "pypi": {
#                "package": "snowflake-connector-python"
#            }
#        }
#    ]
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

echo "======================= Install Databricks Clusters Libraries ======================="

echo "    ==> reading ${path_to_config}"
raw_json=`cat ${path_to_config}`

# get list of clusters
echo "    ==> getting databricks clusters..."
existing_clusters=`databricks clusters list --profile $2 --output JSON | jq -c '. // empty'`

# Loop through each library in json collection
for row in $(echo "${raw_json}" | jq -r '.all_clusters_libraries[] | @base64'); do
    _jq() {
        echo ${row} | base64 --decode | jq -rc ${1}
    }
    
    library=$(_jq '.')

    echo "    ==> installing library [${library}] to all clusters..."
    curl -n -s -H "Authorization: Bearer ${pat}" -H "Content-Type: application/json" -X POST https://${databricks_instance}/api/2.0/libraries/install-library-on-all-clusters -d '{"library":'${library}'}' > /dev/null
    
    
done
echo "============== Completed Pin Databricks Clusters ======================="