import os
from PIL import Image
from logger import log_message

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = os.path.join(script_dir, "..", "output", "extracted_png")
output_dir = os.path.join(script_dir, "..", "output", "combined_png")


def combine_images(image_files, output_path):
    images = [Image.open(f) for f in image_files]
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    # total_height = sum(heights)

    crop_height = images[0].height // 20

    cropped_images = [image.crop((0, 0, image.width, image.height - crop_height)) for image in images]

    cropped_heights = [img.height for img in cropped_images]
    total_cropped_height = sum(cropped_heights)

    combined_image = Image.new("RGB", (max_width, total_cropped_height))

    y_offset = 0
    for image in cropped_images:
        combined_image.paste(image, (0, y_offset))
        y_offset += image.size[1]

    combined_image.save(output_path)


image_files = sorted([os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".png")])

if image_files:
    receipt_name = "_".join(os.path.basename(image_files[0]).split("_")[:-1])
    output_path = os.path.join(output_dir, f"{receipt_name}_combined.png")
    combine_images(image_files, output_path)
else:
    log_message("combine_images.py", "statement", "No PNG files found in the input directory.")