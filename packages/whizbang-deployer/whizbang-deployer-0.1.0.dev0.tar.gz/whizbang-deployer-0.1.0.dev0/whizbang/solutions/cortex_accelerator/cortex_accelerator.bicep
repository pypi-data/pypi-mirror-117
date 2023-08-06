// cortex_accelerator solution template
// version 0.0.0.0

param uniqueResourceNamingSuffix string
param resourceNamingPrefix string
param sqlAdminUsernameSecretName string
param sqlAdminPasswordSecretName string

var subscriptionId = subscription().subscriptionId
var keyvaultName = '${resourceNamingPrefix}-kv-${uniqueResourceNamingSuffix}'
var logAnalyticsWorkspaceName = '${resourceNamingPrefix}-loganalytics-${uniqueResourceNamingSuffix}'



var nsgName = '${resourceNamingPrefix}-nsgdatabricks-${uniqueResourceNamingSuffix}'
var vnetName = '${resourceNamingPrefix}-vnet-${uniqueResourceNamingSuffix}'
var vnetAddressPrefix = '10.160.0.0/22'
var sqlServerName = '${resourceNamingPrefix}-sql-${uniqueResourceNamingSuffix}'
var sqlDbName = '${resourceNamingPrefix}-statedb'
var sqlDwName = '${resourceNamingPrefix}-dw'
var dataFactoryName = '${resourceNamingPrefix}-datafactory-${uniqueResourceNamingSuffix}'
var databricksName = '${resourceNamingPrefix}-databricks-${uniqueResourceNamingSuffix}'

// datalake resource name
var removeDashPrefix = replace(resourceNamingPrefix, '-', '')
var removeDotPrefix = replace(removeDashPrefix, '.', '')

var removeDashSuffix = replace(uniqueResourceNamingSuffix, '-', '')
var removeDotSuffix = replace(removeDashSuffix, '.', '')

var dataLakeName = '${removeDotPrefix}dl${removeDotSuffix}'

var subnets = {
  value: [
    {
        name: 'adbprivate'
        properties: {
            addressPrefix: '10.160.3.0/24'
            networkSecurityGroup: {
                id: '/subscriptions/${subscriptionId}/resourceGroups/${resourceGroup().name}/providers/Microsoft.Network/networkSecurityGroups/${nsgName}'
            }
            serviceEndpoints: []
            delegations: [
                {
                    name: 'databricks-del-private'
                    properties: {
                        serviceName: 'Microsoft.Databricks/workspaces'
                    }
                }
            ]
        }
    }
    {
        name: 'adbpublic'
        properties: {
            addressPrefix: '10.160.2.0/24'
            networkSecurityGroup: {
                id: '/subscriptions/${subscriptionId}/resourceGroups/${resourceGroup().name}/providers/Microsoft.Network/networkSecurityGroups/${nsgName}'
            }
            serviceEndpoints: []
            delegations: [
                {
                    name: 'databricks-del-public'
                    properties: {
                        serviceName: 'Microsoft.Databricks/workspaces'
                    }
                }
            ]
        }
    }
  ]
}

resource keyvault 'Microsoft.KeyVault/vaults@2019-09-01' existing = {
  name: keyvaultName
  scope: resourceGroup()
}

module logAnalytics '../../../modules/loganalytics.bicep' = {
  name: 'logAnalyticsDeploy'
  params: {
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
  }
}

module nsg_databricks '../../../modules/nsg_for_databricks.bicep' = {
  name: 'nsgDatabricksDeploy'
  params: {
    nsgName: nsgName
  }
}

module vnet '../../../modules/vnet_with_diagnostics.bicep' = {
  name: 'vnetDeploy'
  params: {
    vnetName: vnetName
    vnetAddressPrefix: vnetAddressPrefix
    subnets: subnets.value
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
    nsg: nsg_databricks
  }
}

module datalake '../../../modules/datalake_with_diagnostics.bicep' = {
  name: 'datalakeDeploy'
  params: {
    storageAccountName: dataLakeName
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
  }
}

module sqlserver '../../../modules/sqlserver_all_in_one.bicep' = {
  name: 'sqlAllInOneDeploy'
  params: {
    sqlServerName: sqlServerName
    sqlDbName: sqlDbName
    sqlDwName: sqlDwName
    administratorLogin: keyvault.getSecret(sqlAdminUsernameSecretName)
    administratorLoginPassword: keyvault.getSecret(sqlAdminPasswordSecretName)
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
  }
}

module datafactory '../../../modules/datafactory_with_diagnostics.bicep' = {
  name: 'datafactoryDeploy'
  params: {
    dataFactoryName: dataFactoryName
    logAnalyticsWorkspaceName: logAnalyticsWorkspaceName
  }
}

module databricks '../../../modules/databricks.bicep' = {
  name: 'databricksDeploy'
  params: {
    workspaceName: databricksName
    vnetResourceId: vnet.outputs.vnetResourceId
    publicSubnetName: 'adbpublic'
    privateSubnetName: 'adbprivate'
  }
}


output resources object = {
  databricks: databricks
}

output resourceIds object = {
  datalake: datalake.outputs.datalakeResourceId
  databricks: databricks.outputs.databricksResourceId
  vnet: vnet.outputs.vnetResourceId
  sqlserver: sqlserver.outputs.sqlServerResourceId
  datafactory: datafactory.outputs.datafactoryResourceId
}

output resourceNames object = {
  datalake: dataLakeName
  databricks: databricksName
  datafactory: dataFactoryName
  sqlserver: sqlServerName
  vnet: vnetName
  loganalytics: logAnalyticsWorkspaceName
  keyvault: keyvaultName
}

output datalakeName string = dataLakeName
output sqlServerDomain string = sqlserver.outputs.sqlServerDomain
output databricksWorkspaceUrl string = databricks.outputs.workspaceUrl
