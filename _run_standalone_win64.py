import os
import subprocess

from DevOps.scripts.unity_info_module import get_unity_product_name
from DevOps.scripts.unity_info_module import get_unity_install_location

UNITYDIR = get_unity_install_location()
PROJECT_NAME = get_unity_product_name()
PROJECT_DIR = os.path.join(os.path.dirname(__file__))
PROJECT_BIN_DIR = os.path.join(PROJECT_DIR, "Builds")
PROJECT_BIN_WIN64_DIR = os.path.join(PROJECT_BIN_DIR, "StandaloneWindows64")

def find_latest_folder(target_folder):
    folders = sorted(
        [folder for folder in os.listdir(target_folder) if os.path.isdir(os.path.join(target_folder, folder))],
        key=lambda folder: os.path.getmtime(os.path.join(target_folder, folder)),
        reverse=True
    )
    if folders:
        return os.path.join(target_folder, folders[0])
    return None

if __name__ == "__main__":
    print("Started running Standalone Build")

    latest_folder = find_latest_folder(PROJECT_BIN_WIN64_DIR)

    if latest_folder:
        print(f"Latest build found in: {latest_folder}")
        exe_path = os.path.join(latest_folder, f"{PROJECT_NAME}.exe")
        subprocess.run([exe_path, "-log", "-windowed", "-resx=1280", "-resy=720"], shell=True)
    else:
        print(f"No builds found in {PROJECT_BIN_WIN64_DIR}")
