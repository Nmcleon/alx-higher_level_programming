#!/usr/bin/python3
"""
Adds all arguments to a Python list,
and then save them to a file.
"""

import sys
import json

# Define the filename for the JSON file
my_file = 'add_item.json'

# Initialize an empty list or load existing data from the JSON file
try:
    with open(my_file, 'r', encoding='utf-8') as f:
        my_list = json.load(f)
except FileNotFoundError:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
with open(my_file, 'w', encoding='utf-8') as f:
    json.dump(my_list, f)
