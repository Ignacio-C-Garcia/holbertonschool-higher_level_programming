#!/usr/bin/python3
"""comment of the module"""
import requests
from sys import argv


if __name__ == "__main__" and len(argv) == 3:
    response = requests.get(
   'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1]), headers={"Accept": "application/vnd.github.v3+json"})
    response = response.json()
    for x in range(10):
        print('{}: {}'.format(response[x]['sha'], response[x]['commit']['author']['name']))
