#!/usr/bin/python3
"""comment of the module"""
from urllib import request
from urllib import parse
from sys import argv
from urllib import error


if __name__ == "__main__":
	try:
		with request.urlopen(argv[1]) as response:
			body = response.read().decode('utf-8')
			print(body)
	except error.HTTPError as Fail:
		print('Error code:', Fail.code)

