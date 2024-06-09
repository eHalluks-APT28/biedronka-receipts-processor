import subprocess
import os
from logger import log_message

script_dir = os.path.dirname(os.path.abspath(__file__))
services_dir = os.path.join(script_dir, "..", "services")
scripts_dir = os.path.join(script_dir, "..", "scripts")

commands = [
    f"python3 {os.path.join(services_dir, 'pdf_to_png.py')}",
    f"python3 {os.path.join(services_dir, 'combine_images.py')}",
    f"python3 {os.path.join(services_dir, 'prepare_raw_txtFile.py')}",
    f"python3 {os.path.join(services_dir, 'clear_data_in_txt.py')}",
    f"python3 {os.path.join(services_dir, 'prepare_final_json.py')}",
    f"python3 {os.path.join(services_dir, 'find_invalid_objects.py')}"
]

for command in commands:
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        log_message("run_core_process.py", "subprocess.run", f"Command '{command}' failed with error: {e}")