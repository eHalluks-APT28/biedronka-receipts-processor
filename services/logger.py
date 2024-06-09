from datetime import datetime
import os

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "logs.txt")

def log_message(file_name, function_name, message):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"[{current_time}]_[{file_name}]_[{function_name}]: {message}\n")