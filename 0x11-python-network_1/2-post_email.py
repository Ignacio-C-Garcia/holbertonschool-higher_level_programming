#!/usr/bin/python3
"""comment of the module"""
from urllib import request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
