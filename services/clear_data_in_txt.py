import os
import re
from logger import log_message

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_dir, '../output/txt/paragon.txt')
temp_file = os.path.join("/tmp", os.urandom(24).hex())

if not os.path.isfile(input_file):
    log_message("clear_data_in_txt.py", "test path", f"The file: {input_file} does not exist.")
    exit(1)

date_time_found = False
sale_found = False

with open(input_file, 'r') as file, open(temp_file, 'w') as temp:
    lines = file.readlines()
    skip_lines = 0

    for line in lines:
        if skip_lines > 0:
            skip_lines -= 1
            continue

        if not date_time_found:
            if re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}', line):
                date_time_found = True
                temp.write(line)
                skip_lines = 2
        elif not sale_found:
            if re.search(r'[Ss]przeda[zż]', line):
                sale_found = True
            else:
                temp.write(line)

os.system(f"sed -i '/^$/d' {temp_file}")
os.rename(temp_file, input_file)