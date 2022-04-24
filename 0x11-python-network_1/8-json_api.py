#!/usr/bin/python3
"""comment of the module"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = ""

    if len(argv) > 1:
        letter = argv[1]

    response = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        x = response.json()
        if len(x) > 0:
            print('[{}] {}'.format(x['id'], x['name']))
        else:
            print('No result')
    except Exception as fail:
        print('Not a valid JSON')
