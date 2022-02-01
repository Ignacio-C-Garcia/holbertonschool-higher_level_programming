#!/usr/bin/python3
"""name"""


import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    prev = load_from_json_file("add_item.json")
    save_to_json_file(prev + sys.argv[1:], "add_item.json")
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")
