#!/usr/bin/python3
"""comment"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
    print(type(body))
    print(body)
    print(body.decode(encoding='UTF-8'))

