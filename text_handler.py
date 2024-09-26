import os
import subprocess

def save_text_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
    open_file(file_path)

def open_file(file_path):
    if os.name == 'nt':  # Windows
        os.startfile(file_path)
    elif os.uname().sysname == 'Darwin':  # macOS
        subprocess.Popen(['open', file_path])
    else:  # Linux
        subprocess.Popen(['xdg-open', file_path])
