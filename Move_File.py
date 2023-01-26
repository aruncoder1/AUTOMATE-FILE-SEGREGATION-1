import os
import shutil

from_dir = "c:/Users/Admin/Downloads"
to_dir = "c:/User/Admin/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)
#print (list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)