import json


def read_json_file(file_path, key):
    with open(file_path) as f:
        data = json.load(f)
        return data[key]
