import json

def extract_key_value_pairs(path):
    with open(path) as f:
        data = json.load(f)
        key_value_pairs = []

        for key, value in data.items():
            key_value_pairs.append((key, value))

        return key_value_pairs
