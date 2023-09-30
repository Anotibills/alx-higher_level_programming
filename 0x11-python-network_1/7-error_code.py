#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        '''This send a GET request to the provided URL.'''
        response = requests.get(url)

        '''Check the HTTP status code and print messages accordingly.'''
        if response.status_code == 200:
            print(response.text)
        elif response.status_code == 401:
            print("Error code: 401")
        elif response.status_code == 404:
            print("Error code: 404")
        elif response.status_code == 500:
            print("Error code: 500")
        else:
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
