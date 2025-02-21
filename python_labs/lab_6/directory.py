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
# list_items_in_path("/path/to/some/directory")


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
# check_path_access("/path/to/some/file_or_directory")


# Test whether a given path exists. If it does, show its filename and directory portions
