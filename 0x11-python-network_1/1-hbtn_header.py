#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import urllib.request
import sys

'''This checks if a URL is provided as a command-line argument'''
if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    '''
    Use "urllib" to make an HTTP GET request to the provided URL
    '''
    with urllib.request.urlopen(url) as response:
        # Retrieve the headers from the response
        headers = response.info()

        '''It searches for the 'X-Request-Id' header and print its value'''
        x_request_id = headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
            sys.exit(1)

except Exception as e:
    '''This handles any exception'''
    print("Error: {}".format(e))
    sys.exit(1)
