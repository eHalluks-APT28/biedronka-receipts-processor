import os
import pytesseract
from PIL import Image
import cv2
from logger import log_message

script_dir = os.path.dirname(os.path.abspath(__file__))
combined_dir = os.path.join(script_dir, "..", "output", "combined_png")
output_file_path = os.path.join(script_dir, "..", "output", "txt", "paragon.txt")

image_file = None
for file_name in os.listdir(combined_dir):
    if file_name.endswith('.png'):
        image_file = os.path.join(combined_dir, file_name)
        break

if image_file is None:
    log_message("prepare_raw_txtFile.py", "statement",
                "Lack of PNG file in 'output/combined_png'")
    raise FileNotFoundError("Check logs file")

image = Image.open(image_file)

image_cv = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
image_cv = cv2.adaptiveThreshold(image_cv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
image = Image.fromarray(image_cv)

custom_oem_psm_config = r'--oem 3 --psm 6'
extracted_text = pytesseract.image_to_string(image, config=custom_oem_psm_config, lang='pol')

lines = extracted_text.split('\n')
table_lines = []
capture = False

for line in lines:

    if "Nazwa" in line and "Ilość" in line:
        capture = True

    if capture and any(char.isdigit() for char in line):
        table_lines.append(line)

with open(output_file_path, 'w', encoding='utf-8') as output_file:

    output_file.write("Wyodrębniony tekst z obrazu:\n")
    output_file.write(extracted_text)
    output_file.write("\n\n")

    output_file.write("Wyodrębnione linie tabeli:\n")
    output_file.write('\n'.join(table_lines))