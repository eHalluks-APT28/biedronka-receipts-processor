import os
from pdf2image import convert_from_path

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "input")
output_dir = os.path.join(script_dir, "..", "output", "extracted_png")


def convert_pdf_to_png(pdf_path, output_dir):
    images = convert_from_path(pdf_path)
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]

    for i, image in enumerate(images, start=1):
        image_path = os.path.join(output_dir, f"{file_name}_{i}.png")
        image.save(image_path, "PNG")

    return len(images)


for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, filename)
        num_pages = convert_pdf_to_png(pdf_path, output_dir)