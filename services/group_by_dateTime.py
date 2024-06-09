import os
import json
from collections import defaultdict

def load_json_objects(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


script_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(script_dir, "..", "output", "target")
receipts_file_path = os.path.join(target_dir, "receipts.json")

receipts_data = load_json_objects(receipts_file_path)

grouped_receipts = defaultdict(list)
for receipt in receipts_data["receipts"]:
    date_time = receipt["date_time"]
    grouped_receipts[date_time].append(receipt)

grouped_receipts_dict = {
    "receipts": [{"receipt_date_time": date, "items": items} for date, items in grouped_receipts.items()]}

with open(receipts_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(grouped_receipts_dict, output_file, ensure_ascii=False, indent=4)