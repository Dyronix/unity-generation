import os
import subprocess
import argparse

from DevOps.scripts.unity_info_module import get_unity_product_name
from DevOps.scripts.unity_info_module import get_unity_install_location

UNITYDIR = get_unity_install_location()
PROJECT_NAME = get_unity_product_name()
PROJECT_DIR = os.path.join(os.path.dirname(__file__))
PROJECT_BIN_DIR = os.path.join(PROJECT_DIR, "Builds")
PROJECT_BIN_WIN64_DIR = os.path.join(PROJECT_BIN_DIR, "StandaloneWindows64")

def main():
    parser = argparse.ArgumentParser(description="Build Unity project")
    parser.add_argument("-scene_to_build", help="Name of the scene to build")

    args = parser.parse_args()

    # Construct the command
    command = [
        UNITYDIR,
        "-quit",
        "-batchmode",
        "-projectPath", PROJECT_DIR,
        "-executeMethod", "PlayerBuild.PerformWin64Console",
        "-scene_to_build="+args.scene_to_build
    ]

    print(command)

    # Execute the command
    subprocess.run(command)

if __name__ == "__main__":
    main()
