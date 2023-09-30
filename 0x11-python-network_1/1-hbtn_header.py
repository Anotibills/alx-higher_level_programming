#!/usr/bin/python3
"""
This script retrieves and print the X-Requested-Id
"""
import urllib.request
import sys


def get_x_request_id(url):
    try:
        '''Send a request to the provided URL.'''
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        '''
        Check if the correct number of command-line arguments is provided.
        '''
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
