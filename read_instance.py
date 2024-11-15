import json


def read_instance(size: str):
    with open(f"instances/{size}.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
