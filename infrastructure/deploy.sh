#!/bin/bash

# Verify Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "Azure CLI is not installed. Please install it first."
    exit 1
fi

# Check if user is logged in to Azure
echo "Checking Azure login status..."
az account show &> /dev/null || { echo "Please login to Azure using 'az login'"; az login; }

# Get current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get user input for resource group name
echo "Please enter the name of the resource group (or press Enter to use the default 'rg-jmg-containerapp-deploy-test-2'):"
read -r RESOURCE_GROUP_NAME
if [ -z "$RESOURCE_GROUP_NAME" ]; then
    RESOURCE_GROUP_NAME="rg-jmg-containerapp-deploy-test-2"
fi
echo "Using resource group name: $RESOURCE_GROUP_NAME"

# First create the resource group
echo "Creating resource group..."
az group create \
  --name "$RESOURCE_GROUP_NAME" \
  --location "eastus2"

# Deploy the Bicep template at resource group scope
echo "Deploying Bicep template at resource group scope..."
az deployment group create \
  --name "container-app-deployment-$(date +%Y%m%d%H%M%S)" \
  --resource-group "$RESOURCE_GROUP_NAME" \
  --template-file "$SCRIPT_DIR/main.bicep" \
  --parameters "$SCRIPT_DIR/parameters.json" \
  --confirm-with-what-if

# Get deployment output (Container App URL)
echo "Deployment completed"
echo "Container App URL can be found in the deployment outputs"