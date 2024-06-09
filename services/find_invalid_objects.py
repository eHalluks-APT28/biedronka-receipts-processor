import json
import os
import glob
from logger import log_message

script_dir = os.path.dirname(os.path.abspath(__file__))
json_directory = os.path.join(script_dir, "..", "output", "json")

json_files = glob.glob(os.path.join(json_directory, "*.json"))
if not json_files:
    log_message("find_invalid_objects.py", "import json file", "Lack of JSON file in 'output/json")
    raise FileNotFoundError("Check logs file")
input_file_path = json_files[0]

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


def should_remove(item):
    return (
            item.get('product') == 'Nazwa' and
            item.get('quantity') == 'PTU' and
            item.get('price') == 'Cena'
    )


filtered_data = [item for item in data if not should_remove(item)]

with open(input_file_path, 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)
