import yaml
import os
import pathlib


# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
yaml_path = os.path.join(root_file, "yaml_files", "random.yml")
with open(yaml_path, "r") as yaml_file:
    content = yaml.load(yaml_file, Loader=yaml.FullLoader)
print(content)

# Generic path generation
root_file = pathlib.Path(__file__).parent.resolve()
yaml_path = os.path.join(root_file, "yaml_files", "test.yml")

my_data = {"key1": 1, "key2": 2, "key3": 3}
with open(yaml_path, "w") as yaml_file:
    content = yaml.dump(my_data, yaml_file)