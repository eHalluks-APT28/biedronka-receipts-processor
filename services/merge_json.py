import os
import json

def load_json_objects(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


script_dir = os.path.dirname(os.path.abspath(__file__))
collection_dir = os.path.join(script_dir, "..", "output", "collection")
target_dir = os.path.join(script_dir, "..", "output", "target")
output_file_path = os.path.join(target_dir, "receipts.json")

all_receipts = []

for filename in os.listdir(collection_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(collection_dir, filename)
        receipts = load_json_objects(file_path)
        all_receipts.extend(receipts)

os.makedirs(target_dir, exist_ok=True)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump({"receipts": all_receipts}, output_file, ensure_ascii=False, indent=4)