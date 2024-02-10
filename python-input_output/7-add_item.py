#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a file
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Load existing list from file if it exists
try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

# Add arguments to the list
for arg in sys.argv[1:]:
    existing_list.append(arg)

# Save the updated list to the file
save_to_json_file(existing_list, "add_item.json")
