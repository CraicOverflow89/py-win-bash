# mv source target

import os, shutil, sys

# Source File
if len(sys.argv) < 2:
    print("Must supply source file!")
    exit()
file_source = os.getcwd() + "/" + sys.argv[1]
if not os.path.exists(file_source):
    print("Source file does not exist!")
    exit()

# Target File
if len(sys.argv) < 3:
    print("Must supply target file!")
    exit()
file_target = sys.argv[2]

# Move File
shutil.move(file_source, file_target)
