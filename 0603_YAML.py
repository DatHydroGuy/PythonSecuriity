"""
Fix:  Use yaml safe_load()
"""
import yaml

my_file = "yaml_file.yml"
# my_file = "yaml_file_bad.yml"
with open(my_file, 'r') as reader:
    my_data = yaml.safe_load(reader)

print(my_data)
