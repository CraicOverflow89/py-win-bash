# grep pattern [file(s)]
# https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/

import os, sys
from command import Command

# TODO: use next on sys.argv
#       while value starts with - append to options (eg: -i for case-insensitive search)
#       then continue and use next for term and file
#       or use len(option_list) to determine where next element is for term then file

# Iterate Args
# arg_list = iter(sys.argv)
# next(arg_list)

# Parse Options
# option_list = []

# TODO: new decision is to build a list of args (positional), kwargs (eg: -A 10) and flags (eg: -B)
print("DEBUG START")
print(
    Command.parse(
        {
            "kwargs": [
                {"title": "after", "short": "A"},
                {"title": "before", "short": "B"},
            ]
        },
        sys.argv[1:],
    )
)
print("DEBUG END")

# No Term
if len(sys.argv) < 2:
    print("Must supply search term!")
    exit()

# Search Term
search_term = sys.argv[1]

# No File
if len(sys.argv) < 3:
    print("Must supply file pattern!")
    exit()

# file_pattern = sys.argv[2]
# TODO: this argument can also be a pattern that might match many files
#       eg: "abc_*" that matches ["abc_0", "abc_1"]

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
                # TODO: if multiple files are being search then the line needs to show
                #       filename:line text

# Missing File
else:
    print("File does not exist!")
    exit()
