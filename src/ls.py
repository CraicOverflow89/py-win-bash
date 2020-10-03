from math import ceil
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
file_list = list(map(lambda it: it.ljust(name_width), file_list))

# Calculate Dimensions
spacing = "  "
column_count = int(size_cols / (name_width + len(spacing)))
row_count = int(ceil(len(file_list) / column_count))
final_row_cols = column_count - ((column_count * row_count) - len(file_list))

# Create Columns
column_list = []
data = []
for file in file_list:
    data.append(file)
    if len(data) == row_count or (
        len(data) == row_count - 1 and len(column_list) >= final_row_cols
    ):
        column_list.append(data)
        data = []

# Print Rows
for row in range(row_count):
    line = ""
    for column in range(column_count):
        if row == row_count - 1 and column == final_row_cols:
            break
        if len(line) > 0:
            line += spacing
        line += column_list[column][row]
    print(line)
