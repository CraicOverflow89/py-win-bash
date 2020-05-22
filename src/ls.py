import os, shutil

# Output Size
[size_cols, _] = shutil.get_terminal_size(())

# List Files
file_list = os.listdir(os.getcwd())
name_width = 0
for file in file_list:
	if len(file) > name_width:
		name_width = len(file)

# Pad Strings
file_list = map(lambda it: it.ljust(name_width), file_list)

# Create List
output = []
line = ""

# Iterate Files
for file in file_list:

	# Length Exceeded
	if len(line) + len(file) > size_cols:
		output.append(line)
		line = ""

	# Update Line
	if(len(line) > 0):
		line += "  "
	line += file

# Final Line
output.append(line)

# Render Output
for line in output:
	print(line)