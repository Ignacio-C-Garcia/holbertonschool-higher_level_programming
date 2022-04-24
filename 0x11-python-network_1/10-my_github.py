#!/usr/bin/python3
"""comment of the module"""
import requests
from sys import argv


if __name__ == "__main__":
        response = requests.get(
   'https://api.github.com/user', auth=(argv[1], argv[2]))
        if response.status_code >= 400:
            print('None')
        else:
            print(response.json()['id'])
