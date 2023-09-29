#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL, displays the value
"""
import requests
import sys

''' This check if a URL is provided as a command-line argument'''
if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)

except requests.exceptions.RequestException as e:
    '''Handle requests exceptions'''
    print("Error:", e)
