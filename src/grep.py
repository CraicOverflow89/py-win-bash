# grep pattern [file(s)]

import os, sys

# No Term
if len(sys.argv) < 2:
	print("Must supply search term!")
	exit()

# Search Term
search_term = sys.argv[1]

# No Files
if len(sys.argv) < 3:
	print("Must supply file name!")
	exit()

# File Path
file_path = os.getcwd() + "/" + sys.argv[2]

# File Exists
if os.path.exists(file_path):

	# Read File
	with open(file_path) as file_object:
		for line in file_object:
			line = line.rstrip()

			# Found Term
			if search_term in line:
				print(line)

# Missing File
else:
	print("File does not exist!")
	exit()