// main.bicep - Azure Container App deployment
param location string
param acrName string
param containerAppEnvName string
param containerAppName string
param imageName string
param cpuCore string = '0.5'
param memorySize string = '1.0Gi'
param minReplicas int = 1
param maxReplicas int = 3
param targetPort int = 80

resource acrResource 'Microsoft.ContainerRegistry/registries@2024-11-01-preview' = {
  location: location
    name: uniqueString(resourceGroup().id, acrName)
    sku: {
      name: 'Basic'
    }
}

module userManagedIdentity 'br/public:avm/res/managed-identity/user-assigned-identity:0.4.0' = {
  name: 'userManagedIdentity'
  params: {
    location: location
    name: '${containerAppName}-identity'
  }
}

var acrPullRoleDefinitionId = '7f951dda-4ed3-4680-a7ca-43fe172d538d'
resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid('acrUMIRole', acrPullRoleDefinitionId, resourceGroup().id)
  scope: acrResource
  properties: {
    roleDefinitionId: resourceId('Microsoft.Authorization/roleDefinitions', acrPullRoleDefinitionId)
    principalId: userManagedIdentity.outputs.principalId
  }
}

// Create the Log Analytics workspace needed by the Container App Environment
module logAnalyticsEnvironment 'br/public:avm/res/operational-insights/workspace:0.11.1' = {
  name: 'logAnalyticsEnvironment'
  params: {
    name: uniqueString(resourceGroup().id, '${containerAppEnvName}-logs')
    location: location
    skuName: 'PerGB2018'
    dataRetention: 30
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
  }
}

// Create the Container App Environment
module containerAppEnvironment 'br/public:avm/res/app/managed-environment:0.10.0' = {
  name: 'containerAppEnvironment'
  params: {
    location: location
    name: '${uniqueString(resourceGroup().id, containerAppEnvName)}-${containerAppEnvName}'
    logAnalyticsWorkspaceResourceId: logAnalyticsEnvironment.outputs.resourceId
    zoneRedundant: false
    publicNetworkAccess: 'Enabled'
  }
}

module containerApp 'br/public:avm/res/app/container-app:0.13.0' = {
  name: containerAppName
  params: {
    location: location
    name: containerAppName
    environmentResourceId: containerAppEnvironment.outputs.resourceId
    managedIdentities: {
      userAssignedResourceIds: [
        userManagedIdentity.outputs.resourceId
      ]
    }
    scaleMinReplicas: minReplicas
    scaleMaxReplicas: maxReplicas
    ingressExternal: true
    ingressTargetPort: targetPort

    registries: [
      {
        server: acrResource.properties.loginServer
        identity: userManagedIdentity.outputs.resourceId
      }
    ]
    containers: [
      {
        name: containerAppName
        image: imageName
        resources: {
          cpu: cpuCore
          memory: memorySize
        }
      }
    ]
  }
}

output containerAppFqdn string = containerApp.outputs.fqdn
