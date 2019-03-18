"""
Solution:  Use a safer format, such as JSON.
"""
import json

my_data = "This is my test data"

my_file = "data_file.json"
with open(my_file, 'w') as writer:
    json.dump(my_data, writer)

with open(my_file, 'r') as reader:
    new_data = json.load(reader)

print(new_data)
