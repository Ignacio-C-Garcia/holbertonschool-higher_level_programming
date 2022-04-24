#!/usr/bin/python3
"""comment"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print('Body response:')
    body = response.read()
    print('\t- type:', type(body))
    print('\t- content:', body)
    print('\t- utf8 content', body.decode(encoding='UTF-8'))
