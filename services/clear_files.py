import os
import shutil
from logger import log_message

script_dir = os.path.dirname(os.path.abspath(__file__))
directories = [
    os.path.join(script_dir, "..", "output", "combined_png"),
    os.path.join(script_dir, "..", "output", "extracted_png"),
    os.path.join(script_dir, "..", "output", "json"),
    os.path.join(script_dir, "..", "output", "txt"),
]

for dir in directories:
    dir = os.path.abspath(dir)
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            log_message("clear_files.py", "filename variable", f"Failed to delete {file_path}. Reason: {e}")