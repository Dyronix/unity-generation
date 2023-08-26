# unity-generation

How to use

Download or clone the repository on your machine
Copy the contents of the repository (except the .git folder if cloned)
Go to your/project/directory
Paste the contents of the repository within that folder
Happy coding

_run_editor.py

This script will run the editor with the given project version of the project
This script will generate a log file within the Logs folder of the Unity project, the name of the log will be the date of "today" with an index appended to it.

=> MMDDYYYY_INDEX

_run_standalone_win64.py

This script will run the latest build found within the Builds folder.
If no build was found nothing is run.

_build_standalone_win64.py

This script will generate a new build for a given scene.
Note: This will only work for scenes that have been added to the build window within the Unity Editor

=> py ./_build_standalone_win64.py -scene_to_build=name_of_scene
