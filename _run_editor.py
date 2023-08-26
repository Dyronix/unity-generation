import os
import subprocess
import datetime

from DevOps.scripts.unity_info_module import get_unity_product_name
from DevOps.scripts.unity_info_module import get_unity_install_location

UNITYDIR = get_unity_install_location()
PROJECT_NAME = get_unity_product_name()
PROJECT_DIR = os.path.join(os.path.dirname(__file__))
PROJECT_BIN_DIR = os.path.join(PROJECT_DIR, "Builds")
PROJECT_BIN_WIN64_DIR = os.path.join(PROJECT_BIN_DIR, "StandaloneWindows64")

# Get the current date
current_date = datetime.datetime.now()
day = str(current_date.day).zfill(2)
month = str(current_date.month).zfill(2)
year = str(current_date.year)

# Create a formatted date string
formatted_date = day + month + year
base_log_filename = formatted_date
index = 0

while True:
    # Check for existing log files with an incremental index
    log_filename = f"{base_log_filename}_{index}.txt"
    if os.path.exists(os.path.join(PROJECT_DIR, "Logs", log_filename)):
        index += 1
    else:
        break

# Generate a unique log file name
log_filename = f"{base_log_filename}_{index}.txt"

print(log_filename)

print("Started running Unity Editor")
subprocess.call([UNITYDIR, "-projectPath", PROJECT_DIR, "-logFile", os.path.join(PROJECT_DIR, "CustomLog", log_filename)])
