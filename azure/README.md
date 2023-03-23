# Introduction 
Folder contains resources to demonstrate Konnect CICD using Azure DevOps. Contains three pipelines
    -  `azure-pipelines.yaml` which will perform `decK ping`, `decK validate`, `decK diff` and `decK sync` in non production environments.
    -  `azure-pipelines-prod.yaml` which will perform `decK ping`, `decK validate`, `decK diff` and `decK sync` in production environments.
    - `deck-dump-pipeline.yaml` which will perform `decK ping` and `decK dump`

# Pre-requisites
1. Azure DevOps Environment access
2. Access to this repository
3. Create variable group for non production environment in Pipelines Library section of Azure DevOps. **Note**: In this repo, `kong-nonprod` variable is created and used, make sure to update the `azure-pipelines.yaml` and `deck-dump-pipeline.yaml` with the group name created here. 
    - Create two variables
        - konnect-token (Value for this will be personal access token)
        - konnect-addr (Address of the Konnect endpoint)
4. Create variable group for production environment in Pipelines Library section of Azure DevOps. **Note**: In this repo, `kong-prod` variable is created and used, make sure to update the `azure-pipelines-prod.yaml` with the group name created here. 
    - Create two variables
        - konnect-token (Value for this will be personal access token)
        - konnect-addr (Address of the Konnect endpoint)

# Create and Execute Non-Prod Pipeline
- Create a new pipeline using the `azure-pipelines.yaml` file located in the repository.
- Run the pipeline created by defining values for following parameters.
    - Choose the branch
    - Select Konnect runtime group
    - Give name of the Konnect/Kong Service
    - Check `Sync configurations to Konnect` if configurations have to be deployed to Konnect. By default this is set to false, which means pipeline doesn't sync configurations to Konnect, instead it will just show perform `decK ping, validate and diff`
    - Click on Run to trigger pipeline execution against the defined service and environment.

# Create and Execute Prod Pipeline
- Create a new pipeline using the `azure-pipelines-prod.yaml` file located in the repository.
- Run the pipeline created by defining values for following parameters.
    - Choose the branch
    - Select Konnect runtime group
    - Give name of the Konnect/Kong Service
    - Click on Run to trigger pipeline execution against the defined service and environment.