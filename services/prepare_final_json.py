import json
import os

def rename_file(old_filename):
    date_part, time_part = old_filename.split()
    day, month, year = date_part.split('.')
    formatted_date = f"{year}-{month}-{day}"
    formatted_time = time_part.replace(':', '-')
    new_filename = f"{formatted_date}_{formatted_time}"
    return new_filename

def extract_file_name(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
    return first_line

def parse_line(line):
    parts = line.split()
    if len(parts) < 5:
        return None
    product = ' '.join(parts[:-4])
    quantity = parts[-4]
    price = parts[-2]
    value = parts[-1]
    return {
        "product": product,
        "quantity": quantity,
        "price": price,
        "value": value,
        "category": ""
    }

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_dir, "..", "output", "txt", "paragon.txt")
    file_name = extract_file_name(input_file_path)
    output_file_path = os.path.join(script_dir, "..", "output", "json", f"{rename_file(file_name)}.json")
    objects = []

    with open(input_file_path, 'r', encoding='utf-8') as file:
        date_time = file.readline().strip()
        current_obj = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("Rabat"):
                rabat_value = file.readline().strip()
                if current_obj:
                    current_obj["value"] = rabat_value
                    objects.append(current_obj)
                current_obj = None
            else:
                if current_obj:
                    objects.append(current_obj)
                current_obj = parse_line(line)
                if current_obj:
                    current_obj["date_time"] = date_time
        if current_obj:
            objects.append(current_obj)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(objects, output_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
