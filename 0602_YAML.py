"""
YAML contains pre-processing directives which allow structured data to be serialised / de-serialised.
These directives can lead to arbitrary code execution.
One such exploit was found in the popular automation software Ansible.  See the following link:
https://www.talosintelligence.com/reports/TALOS-2017-0305
"""
import yaml

# my_file = "yaml_file.yml"
my_file = "yaml_file_bad.yml"
with open(my_file, 'r') as reader:
    my_data = yaml.load(reader)

print(my_data)
