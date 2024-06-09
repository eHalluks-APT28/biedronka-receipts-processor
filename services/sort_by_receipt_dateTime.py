import os
import json
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(script_dir, "..", "output", "target")
output_file_path = os.path.join(target_dir, "receipts.json")


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Wczytaj dane
data = load_json(output_file_path)

if len(data['receipts']) > 1:
    data['receipts'].sort(key=lambda x: datetime.strptime(x['receipt_date_time'].split()[0], '%d.%m.%Y'))
save_json(output_file_path, data)