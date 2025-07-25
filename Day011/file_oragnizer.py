## >>>>>>>>>> SIMPLE FILE ORGANIZER <<<<<<<<<<<

import os
import shutil

source_dir = input("Enter directory to organize: ")

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}

for file in os.listdir(source_dir):
    name, ext = os.path.splitext(file)
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            folder_path = os.path.join(source_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(os.path.join(source_dir, file), os.path.join(folder_path, file))
            break
