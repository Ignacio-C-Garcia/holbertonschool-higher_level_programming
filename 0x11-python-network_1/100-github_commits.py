#!/usr/bin/python3
"""comment of the module"""
import requests
from sys import argv


if __name__ == "__main__" and len(argv) == 3:
    response = requests.get(
   'https://api.github.com/repos/{}/{}/commits'.format(
       argv[2], argv[1]), headers={"Accept": "application/vnd.github.v3+json"})
    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        try:
            response = response.json()
        except Exception as f:
            print('None')
        rep = 10
        if len(response) < 10:
            rep = len(response)
        for x in range(rep):
            print('{}: {}'.format(
                response[x]['sha'], response[x]['commit']['author']['name']))
