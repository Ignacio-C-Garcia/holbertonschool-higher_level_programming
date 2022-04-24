#!/usr/bin/python3
"""comment of the module"""
import requests


if __name__ == "__main__":
	response = requests.get('https://intranet.hbtn.io/status')
	print('Body response:')
	print('\t- type:', type(response.text))
	print('\t- content:', response.text)
