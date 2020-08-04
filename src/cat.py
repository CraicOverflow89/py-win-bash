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

		# Read File
		with open(file_path) as file_object:
			for line in file_object:
				print(line.rstrip())

	# Missing File
	else:
		print("File does not exist!")
		exit()