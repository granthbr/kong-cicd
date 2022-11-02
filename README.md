# Introduction 
Repository that contains resources to demonstrate Konnect/Kong CICD (Right now we only have Azure DevOps pipeline, will be adding more soon). Contains a pipeline `azure-pipelines.yaml` which will perform `decK ping`, `decK validate`, `decK diff` and `decK sync`. 

# Repository Explanation

| File/Folder | Description |
| --- | ----------- |
| `kong` | Contains environment specific folders with different service specific values file specific to that environment. |
| `results` | Added a dummy file, but this is the folder where the processed yaml files get created by `generate_yaml.py` |
| `templates` | Contains the jinja2 template files specific to services. |
| `azure` | Azure DevOps pipeline resources, README.md |
| `generate_yaml.py` | Python script to process the jinga2 templates. |
| `README.md` | Repository specific README file. |

# Create and Execute Pipeline
 - Refer `azure` folder for details.
 - In future will add references for other CICD tools.

# On-board a new Service
 - Create a `template` jinja2 file in `templates` folders
   - Easy way to create a template file is
     - Manually create service in Konnect Cloud
     - Execute `deck dump` command with appropriate tags to only get the content of your service.
     - Update the file with `jinga2` syntax for the values those are not static and should be overridden by values from `kong/<environment folder>/<servicename_environment>.yaml`
 - Create value(s) file in `kong` folder
 - Commit changes to repository

# To process jinga2 template locally
- Following tools have to be installed.
    1. jinga2
    2. PyYaml
    3. python3
- Set two environment variables
    1. KONNECT_RUNTIME_GROUP
    2. KONNECT_SERVICE_NAME
- Excute following `generate_yaml.py` file in command line. Example command: `python3 generate_yaml.py`
- Once executed, the generated yaml file can be found in `results` folder.