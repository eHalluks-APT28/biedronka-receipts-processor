import os
import shutil
import sys
import subprocess
from services.logger import log_message

################################################################
# Remove below block after cloned
################################################################

directories = [
    "input",
    "output/collection",
    "output/combined_png",
    "output/extracted_png",
    "output/json",
    "output/target",
    "output/txt",
    "receipts/done",
    "receipts/downloaded"
]

for directory in directories:
    gitkeep_path = os.path.join(directory, ".gitkeep")
    if os.path.isfile(gitkeep_path):
        os.remove(gitkeep_path)

################################################################
# end of block of code to remove
################################################################


def initial_check_in():
    required_paths = [
        "input",
        "logs",
        "logs/logs.txt",
        "output",
        "output/collection",
        "output/combined_png",
        "output/extracted_png",
        "output/json",
        "output/target",
        "output/txt",
        "receipts",
        "receipts/done",
        "receipts/downloaded",
        "services"
    ]

    missing_elements = [path for path in required_paths if not os.path.exists(path)]

    if missing_elements:
        print ("[ CRITICAL ERROR ] : Missing the most important elements. Please verify structure")
        exit(1)

def check_existing_dir(directory):
    return os.path.exists(directory)


def check_files_in_dir(directory):
    return any(os.path.isfile(os.path.join(directory, f)) for f in os.listdir(directory))


def count_files_in_dir(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])


def move_first_file(source_directory, target_directory):
    files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]
    if not files:
        return False

    first_file = files[0]
    source_path = os.path.join(source_directory, first_file)
    target_path = os.path.join(target_directory, first_file)
    shutil.move(source_path, target_path)
    return True


def print_progress_bar(iteration, total, length=50):
    percent = round(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '\033[92m' + '█' * filled_length + '\033[0m' + '-' * (length - filled_length)
    print(f'\r  Progress: | {bar} | {percent}% Complete', end='\r')
    if iteration == total:
        print()


initial_file_count = count_files_in_dir("receipts/downloaded")

if check_existing_dir("receipts/downloaded") and check_files_in_dir("receipts/downloaded"):

    print("\n")
    while check_files_in_dir("receipts/downloaded"):
        move_first_file("receipts/downloaded", "input/")
        subprocess.run(['python3', 'services/run_core_process.py'])
        if check_files_in_dir("output/json"):
            move_first_file("output/json", "output/collection")
        subprocess.run(['python3', 'services/clear_files.py'])
        move_first_file("input/", "receipts/done")
        processed_files = initial_file_count - count_files_in_dir("receipts/downloaded")
        print_progress_bar(processed_files, initial_file_count)

    subprocess.run(['python3', 'services/merge_json.py'])
    subprocess.run(['python3', 'services/group_by_dateTime.py'])
    subprocess.run(['python3', 'services/sort_by_receipt_dateTime.py'])

    print('\r' + ' ' * 80 + '\r', end='\n')
    print("\n  The process has been completed successfully\n  Please check: '\033[92moutput/target\033[0m' directory.\n")

else:
    log_message("main.py", "Initial statement", "CRITICAL: The downloaded directory does not exist or is empty.")
    sys.exit()