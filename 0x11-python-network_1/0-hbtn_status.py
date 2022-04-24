#!/usr/bin/python3
"""comment of the module"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print('Body response:')
        body = response.read()
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content {}'.format(body.decode(encoding='UTF-8')))
