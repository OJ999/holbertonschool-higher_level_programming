#!/usr/bin/python3
import sys
from os.path import exists
from json import dumps, loads
from contextlib import suppress

# Function to save data to a JSON file
def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        f.write(dumps(my_obj))

# Function to load data from a JSON file
def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return (loads(f.read()))

# Check if the file exists, if not create it
filename = 'add_item.json'
if not exists(filename):
    with open(filename, 'w'):
        pass

# Load existing data from the file
try:
    data = load_from_json_file(filename)
except:
    data = []

# Add command-line arguments to the data
data.extend(sys.argv[1:])

# Save the updated data to the file
save_to_json_file(data, filename)
