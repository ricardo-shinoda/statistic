import zipfile
import shutil
import subprocess
import os

# Path to the downloaded zip file
# Replace with the actual file path
zip_file_path = "/home/ricardo/Downloads/Fatura-CPF.zip"

# Password for the zip file
zip_password = "218843"

# Extract the contents of the zip file
# Replace with the desired extraction folder
extracted_folder = "/home/ricardo/Downloads/"
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder, pwd=bytes(zip_password, 'utf-8'))

# Path to the extracted text file
# Replace with the actual file name
extracted_text_file = os.path.join(extracted_folder, "Fatura_2023-09-10.csv")

# Path to the Text Editor app in Pop OS
# Replace with the actual path to the Text Editor app
text_editor_path = "/usr/bin/gedit"

# Open the text file with the Text Editor app
subprocess.run([text_editor_path, extracted_text_file])

# Move the text file to the desktop folder
# Replace with the desired desktop folder
desktop_folder = "/home/ricardo/Desktop/test"
shutil.move(extracted_text_file, desktop_folder)

# Clean up: remove only the zip file
os.remove(zip_file_path)
