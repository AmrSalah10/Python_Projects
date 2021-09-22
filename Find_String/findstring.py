# Search For specific string inside files which inside folders
import os

# Get text to search for from user
text = input('input text: ')

# Get parent folder name to search in its children
folder = input('folder: ')

# Get the folder path
absolute_path = os.path.abspath(folder)

# Recursive iteration inside the folder files and sub-folders' files
def get_files(path):
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path ,file)
            if os.path.isdir(file_path):
                os.chdir(file_path)
                check_dir = get_files(file_path)
                if 'found in' in check_dir:
                    return check_dir
            else:
                with open(file, 'r') as f:
                    if text in f.read():
                        final_path = os.path.abspath(file)
                        return (text + " found in " + final_path)
        return text + ' is not found'
    else:
        return('This path is not valid')

print(get_files(absolute_path))
