# Python Find text in files from specified directory
# The application searches for a specified text in any files within a given directory


import os

user_text = input("Type the text: ")
user_path = input("Type the path name: ")


def search_files_in_directory(path_name, text):
    # Retrieves file names
    files = os.listdir(path_name)
    for file in files:
        # Retrieves the absolute path
        abs_path = os.path.join(path_name, file)

        # If the file is not a directory, searches the specified text
        if os.path.isfile(abs_path):
            search_text_in_file(abs_path, text)

        # If the file is a directory, recalls the function recursively on the specified directory
        if os.path.isdir(abs_path):
            search_files_in_directory(abs_path, text)


def search_text_in_file(path_name, text):
    try:
        # Read data from the file and checks if it contains the specified text
        with open(path_name, "r") as f:
            if text in f.read():
                print(f"The string: '{text}' was found in {path_name}")
    # Handles errors
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)


search_files_in_directory(user_path, user_text)
