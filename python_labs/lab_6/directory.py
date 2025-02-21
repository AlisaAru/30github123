# List only directories, only files, and all items in a specified path

import os

def list_items_in_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    all_items = os.listdir(path)
    only_files = []
    only_dirs = []

    for item in all_items:
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            only_files.append(item)
        elif os.path.isdir(full_path):
            only_dirs.append(item)

    print(f"All items in '{path}':")
    print(all_items)

    print(f"\nOnly directories in '{path}':")
    print(only_dirs)

    print(f"\nOnly files in '{path}':")
    print(only_files)

# Example usage:
# list_items_in_path("python_labs\\lab_6")


# Check for access to a specified path

def check_path_access(path):
    print(f"Testing path: {path}")
    
    if os.access(path, os.F_OK):
        print("  Exists: YES")
    else:
        print("  Exists: NO")
        return  
    
    # Readable?
    if os.access(path, os.R_OK):
        print("  Readable: YES")
    else:
        print("  Readable: NO")
    
    # Writable?
    if os.access(path, os.W_OK):
        print("  Writable: YES")
    else:
        print("  Writable: NO")
    
    # Executable?
    if os.access(path, os.X_OK):
        print("  Executable: YES")
    else:
        print("  Executable: NO")

# Example usage:
# check_path_access("python_labs\\lab_6")


# Test whether a given path exists. If it does, show its filename and directory portions

def test_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        file_name = os.path.basename(path)
        directory_name = os.path.dirname(path)
        
        print(f"  File name portion: {file_name}")
        print(f"  Directory portion: {directory_name}")
    else:
        print(f"Path does not exist: {path}")

# Example usage:
# test_path("python_labs\\lab_6")
# test_path("python_labs\\lab_6\\tect.txt")


# Count the number of lines in a text file

def count_lines_in_file(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return 0

    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for _ in file:
            line_count += 1

    return line_count

# Example usage:
# filename = "output.txt"
# print(f"Number of lines in '{filename}': {count_lines_in_file(filename)}")

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)


# Write a list to a file

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data_list:
            f.write(str(item) + "\n")

# Example usage:
# data = ["First line", "Second line", "Third line"]
# write_list_to_file("output.txt", data)


# Generate 26 text files named A.txt through Z.txt
import string

def generate_alphabet_files(directory):
    # Ensure directory exists (optional)
    os.makedirs(directory, exist_ok=True)

    for letter in string.ascii_uppercase:  # A-Z
        file_name = f"{letter}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"This is file {file_name}\n")  # Example content

    print(f"Generated files A.txt through Z.txt in '{directory}'.")

# Example usage:
# generate_alphabet_files("python_labs\\lab_6")


# Copy the contents of one file to another file
def copy_file_contents(src, dest):
    if not os.path.exists(src):
        print(f"Source file '{src}' does not exist.")
        return

    with open(src, 'r', encoding='utf-8') as f_src, \
         open(dest, 'w', encoding='utf-8') as f_dest:
        for line in f_src:
            f_dest.write(line)

    print(f"Copied contents from '{src}' to '{dest}'.")

# Example usage:
copy_file_contents("copy_from.txt", "copy_to.txt")


# Delete a file by a specified path (check access/existence first)

def delete_file(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' does not exist.")
        return
    
    if not os.path.isfile(file_path):
        print(f"'{file_path}' is not a file.")
        return

    if not os.access(file_path, os.W_OK):
        print(f"No permission to delete file '{file_path}'.")
        return

    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

# Example usage:
delete_file("deleted.txt")