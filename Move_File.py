import os
import shutil
from_dir="C:/Users/MUSTU/Documents"
to_dir="C:/Users/MUSTU/Downloads"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    print("Moving" + filename)