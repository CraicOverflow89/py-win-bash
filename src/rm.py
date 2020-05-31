import os, sys

# No File
if len(sys.argv) < 2:
	print("Must supply file name!")
	exit()

# NOTE: when adding flags, pos 1 will be -[r|f]
#       and pos 2 will be file name

# File Path
file_path = os.getcwd() + "\\" + sys.argv[1]

# File Exists
if os.path.exists(file_path):

	# Remove Directory
	if os.path.isdir(file_path):
		os.rmdir(file_path)
		# NOTE: if directory with contents then don't delete unless flags are present
		#       and a different method is required

	# Remove File
	else:
		os.remove(file_path)