import os
import sys
from datetime import datetime

def add_date_to_filenames(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
        return

    # Format today's date as YYYY-MM-DD
    today_str = datetime.today().strftime('%Y-%m-%d')
    print(f"Prepending today's date ({today_str}) to files in: {folder_path}\n")

    renamed_count = 0
    # List files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if not os.path.isfile(file_path):
            continue
            
        # Avoid double-prepending if the file already starts with today's date
        if filename.startswith(today_str):
            print(f"Skipped (already prefixed): {filename}")
            continue
            
        # Construct new filename
        new_filename = f"{today_str}_{filename}"
        new_file_path = os.path.join(folder_path, new_filename)
        
        try:
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")
            renamed_count += 1
        except Exception as e:
            print(f"Error renaming {filename}: {e}")
            
    print(f"\nCompleted! Renamed {renamed_count} files.")

if __name__ == "__main__":
    # Use folder from command-line argument if provided, otherwise default to './test_files'
    folder = sys.argv[1] if len(sys.argv) > 1 else './test_files'
    add_date_to_filenames(folder)
