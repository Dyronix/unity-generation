import os
import re

# Replace with actual file paths
_project_version_file_path = "ProjectSettings/ProjectVersion.txt"
_project_settings_file_path = "ProjectSettings/ProjectSettings.asset"

def __extract_value_from_file(file_path, pattern, error_message):
    """
    Extracts a value from a file using a given regular expression pattern.

    Args:
        file_path (str): Path to the file.
        pattern (str): Regular expression pattern to match.
        error_message (str): Error message to display if the value is not found.

    Returns:
        str: The extracted value if found, otherwise returns None.
    """
    try:
        # Read the content from the file
        with open(file_path, "r") as file:
            file_content = file.read()

        # Extract the value using regular expression
        match = re.search(pattern, file_content)

        if match:
            extracted_value = match.group(1)
            return extracted_value
        else:
            print(f"Error: {error_message}")
            return None
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def __extract_product_name(file_path):
    pattern = r"productName:\s+(.+)"
    error_message = "Product Name not found."
    return __extract_value_from_file(file_path, pattern, error_message)

def __extract_editor_version(file_path):
    pattern = r"m_EditorVersion:\s+(.+)"
    error_message = "Editor Version not found."
    return __extract_value_from_file(file_path, pattern, error_message)

def __make_unity_install_path(version):
    """
    Gets the Unity installation path for a given version.

    Args:
        version (str): The Unity editor version.

    Returns:
        str: The installation path if found, otherwise returns None.
    """
    unity_install_path = rf"C:\Program Files\Unity\Hub\Editor\{version}\Editor\Unity.exe"
    if os.path.exists(unity_install_path):
        return unity_install_path
    else:
        return None
    
# This function is designed to retrieve the name of a Unity project/product
# by extracting it from a project settings file.

# To use this function, make sure you have the actual file path of your Unity
# project settings file stored in the variable _project_settings_file_path.

# The function will attempt to extract the product name using an internal
# function called __extract_product_name().

# If the extraction is successful and a product name is found, the function
# will print the product name and return it.

# If no product name is extracted, the function will print an error message
# and return None, indicating that the product name couldn't be determined.

# Example usage:
# product_name = get_unity_product_name()
# if product_name:
#     print("Product Name:", product_name)
# else:
#     print("Failed to retrieve the product name.")
def get_unity_product_name():
    file_path = _project_settings_file_path  # Replace with the actual file path
    extracted_name = __extract_product_name(file_path) # Call the internal function to extract product name

    # Check if a product name was successfully extracted
    if extracted_name:
        print("Product Name:", extracted_name) # Print the extracted product name
        return extracted_name # Return the extracted product name
    
    # If no product name was extracted, indicate an error and stop the script
    print("Error: Product Name is None, stopping script")
    return None # Return None to indicate the absence of a product name

# This function is designed to help retrieve the installation path of a specific
# version of Unity, along with its corresponding editor version.

# To use this function, ensure you have the actual file path of your Unity
# project version file stored in the variable _project_version_file_path.

# The function will first attempt to extract the editor version from the provided
# version file using an internal function called __extract_editor_version().

# If the extraction is successful, it will attempt to generate the Unity
# installation path based on the extracted editor version using another internal
# function called __make_unity_install_path().

# If the installation path can be generated automatically, the function will
# print it and return it.

# If the automatic generation of the installation path fails, the function will
# prompt the user to provide the Unity installation path. If the provided path
# exists, it will be saved in a file for future reference.

# If the provided user path doesn't exist or if there's an error, the function
# will indicate the issue and return None.

# Example usage:
# unity_install_path = get_unity_install_location()
# if unity_install_path:
#     print("Unity Installation Path:", unity_install_path)
# else:
#     print("Failed to retrieve the Unity installation path.")
def get_unity_install_location():
    # Check if a Unity installation path is stored in the ProjectVersionInstall.txt file
    if os.path.exists("ProjectSettings/ProjectVersionInstall.txt"):
        with open("ProjectSettings/ProjectVersionInstall.txt", "r") as install_file:
            for line in install_file:
                if line.startswith("UnityInstallPath:"):
                    saved_path = line[len("UnityInstallPath:"):].strip()
                    if os.path.exists(saved_path):
                        print("Using stored Unity installation path:", saved_path)
                        return saved_path

    file_path = _project_version_file_path  # Replace with the actual file path
    extracted_version = __extract_editor_version(file_path)  # Extract Unity editor version from a file
    
    # Check if a valid editor version is successfully extracted
    if extracted_version:
        print("Editor Version:", extracted_version)  # Print the extracted editor version
    else:
        # If no editor version is extracted, indicate an error and stop the script
        print("Error: Editor Version is None.")
        print("Unity install location could not be generated, stopping script")
        return None
    
    # Attempt to generate the Unity installation path based on the extracted version
    unity_install_path = __make_unity_install_path(extracted_version)
    
    # If the Unity installation path is successfully generated, print it and return it
    if unity_install_path:
            print("Unity Directory:", unity_install_path)
            return unity_install_path
    else:
        # If the Unity installation path cannot be generated automatically,
        # prompt the user for the path and handle the input
        user_path = input("Unity installation path not found. Please provide the path: ")
        
        # If the provided user path exists, save it in a file and return it
        if os.path.exists(user_path):
            with open("ProjectSettings/ProjectVersionInstall.txt", "w") as install_file:
                install_file.write(f"UnityInstallPath: {user_path}")
            print("Unity installation path saved.")

            return user_path
        
    # If the provided user path doesn't exist, indicate an error and return None
    print("Error: The requested version is not found in the provided path.")
    return None