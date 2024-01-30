# Python Find text in files from specified directory
# The application searches for a specified text in any text files within a given directory


import os

text = input("Type the text: ")
path_name = input("Type the path name: ")


def get_files(path, found=False):
    files = os.listdir(path)
    for file in files:
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):
            try:
                f = open(abs_path, "r")
                if text in f.read():
                    found = True
                    print(f"The string: '{text}' was found in {file}")
            except FileNotFoundError as fe:
                print(fe)
            except PermissionError as pe:
                print(pe)
            except Exception as e:
                print(e)
        if os.path.isdir(abs_path):
            get_files(abs_path)

    return found


if get_files(path_name) is False:
    print(f"The string: '{text}' was not found in any files :(")
