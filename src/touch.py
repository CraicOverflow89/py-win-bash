import os, sys

# No Files
if len(sys.argv) < 2:
	print("Must supply file name(s)!")
	exit()

# Iterate Files
file_list = iter(sys.argv)
next(file_list)
for file in file_list:

	# File Path
	file_path = os.getcwd() + "/" + file

	# File Exists
	if os.path.exists(file_path):

		# Update Timestamp
		os.utime(file_path)

	# Create File
	else:
		with open(file_path, "w") as file_new:
			file_new.write("")