# Introduction 
Repository contains resources to demonstrate Konnect/Kong CICD (Right now only Azure DevOps pipelines are available, will be adding more soon.)

# Repository Explanation

| File/Folder | Description |
| --- | ----------- |
| `kong` | Contains environment specific folders with different service specific values file specific to that environment. |
| `results` | This folder is not present in remote repository, but this is the folder where the processed yaml files get created by `generate_yaml.py` during runtime |
| `dump` | This folder is not present in repository, but this is the folder where we place deck yaml file during deck dump pipeline execution |
| `templates` | Contains the jinja2 template files specific to services. |
| `azure` | Azure DevOps pipeline resources, README.md |
| `generate_yaml.py` | Python script to process the jinga2 templates. |
| `README.md` | Repository specific README file. |

# Create and Execute Azure Pipelines
 - Refer `azure` folder for details.
 
 **Note:** In future will add references for other CICD tools.

# On-board a new Service
 - Create a `template` jinja2 file in `templates` folders
   - Easy way to create a template file is
     - Manually create service in Konnect Cloud
     - Execute `deck dump` command with appropriate tags to only get the content of your service.
     - Update the file with `jinja2` syntax for the values those are not static and should be overridden by values from `kong/<environment folder>/<servicename_environment>.yaml`
 - Create value(s) file in `kong` folder
 - Commit changes to repository

# To process jinga2 template locally(Konnect)
- Following tools have to be installed.
    1. jinja2
    2. PyYaml
    3. python3
- Set two environment variables
    1. KONNECT_RUNTIME_GROUP
    2. KONNECT_SERVICE_NAME
- Excute following `generate_yaml.py` file in command line. Example command: `python3 generate_yaml.py`
- Once executed, the generated yaml file can be found in `results` folder.