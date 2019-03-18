"""
YAML is a human-readable data serialisation standard.
"""
import yaml

my_data = "This is my test data"

my_file = "yaml_file.yml"
with open(my_file, 'w') as writer:
    yaml.dump(my_data, writer)
