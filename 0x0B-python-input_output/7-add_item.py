#!/usr/bin/python3
"""
A module that defines a script
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = \
    __import__("6-load_from_json_file").load_from_json_file
try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    data = []
if len(sys.argv) > 1:
    data = data + sys.argv[1:]

save_to_json_file(data, "add_item.json")
