import os
import yaml
from jinja2 import Environment, FileSystemLoader

konnect_service_name = os.environ.get('KONNECT_SERVICE_NAME')
konnect_runtime_group = os.environ.get('KONNECT_RUNTIME_GROUP')

file_name = './kong/{0}/{1}_{2}.yaml'.format(konnect_runtime_group,konnect_service_name, konnect_runtime_group)
results_file_name = os.getcwd() + "/results/{0}_{1}.yaml".format(konnect_service_name, konnect_runtime_group)

with open(file_name, 'r') as file:
    values = yaml.safe_load(file)
    # Load templates file from templtes folder
    env = Environment(loader = FileSystemLoader('./templates'),   trim_blocks=True, lstrip_blocks=True)
    
    template = env.get_template('{0}.yaml.j2'.format(konnect_service_name))
    file=open(results_file_name, "w")
    file.write(template.render(values))
    file.close()

    with open(results_file_name) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)
        f.close()