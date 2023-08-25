import os

# Counter for deleted elements
deleted_count = 0

# Determine if a file should be deleted
def should_delete(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        if not first_line or first_line.strip() == "<!DOCTYPE html>":
            return True
    return False

# Process directory recursively
def process_directory(directory):
    global deleted_count
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            if should_delete(item_path):
                os.remove(item_path)
                deleted_count += 1
        elif os.path.isdir(item_path):
            process_directory(item_path)

# Execute the script in directories with numeric structure (years)
for dir_name in os.listdir():
    if len(dir_name) == 4 and dir_name.isdigit():
        dir_path = os.path.join(os.getcwd(), dir_name)
        if os.path.isdir(dir_path):
            process_directory(dir_path)

print(f"Deleted {deleted_count} files.")