import tempfile
import os
import csv

trans_tmp = tempfile.mkdtemp()

data = [
    ["key", "en", "ja"]
]
trans_data = {}

def set_trans_text(key: str, text: str) -> None:
    global data
    data.append([key, text, ""])

def get_trans_text(key: str) -> str:
    return trans_data[key]

def write_data() -> str:
    path = os.path.join(trans_tmp, "data.csv")
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        return path

def read_data() -> None:
    path = os.path.join(trans_tmp, "data.csv")
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            trans_data[row[0]] = row[2]
