#!/usr/bin/python3
"""comment of the module"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
        print('\t- utf8 content:', body.decode('utf-8'))
