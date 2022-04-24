#!/usr/bin/python3
"""comment of the module"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
