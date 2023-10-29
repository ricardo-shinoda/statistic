# This is going to be the file to search for an invoice on Downloads page on My computer
# and move it to this repository
import os
import shutil

source_directory = "/home/ricardo/Downloads"

target_file = "invoice.csv"

destination_directory = "/home/ricardo/code/statistic/src"

for root, dirs, files in os.walk(source_directory):
    if target_file in files:
        source_file_path = os.path.join(root, target_file)
        destination_file_path = os.path.join(destination_directory, target_file)
        shutil.move(source_file_path, destination_file_path)

        print(f"File '{target_file}' has been moved to {destination_directory}")
        break