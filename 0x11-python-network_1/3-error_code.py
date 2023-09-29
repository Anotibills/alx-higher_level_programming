#!/usr/bin/python3
''' script that takes in a URL, sends a request to the URL'''
import urllib.request
import sys

'''This check if a URL is provided as a command-line argument'''
if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    '''Use 'urllib' to make an HTTP GET request to the provided URL'''
    with urllib.request.urlopen(url) as response:
        # Read the response body as bytes
        html = response.read()

        '''This print the decoded response content as a string (utf-8)'''
        print(html.decode('utf-8'))

except urllib.error.HTTPError as e:
    '''This handle HTTP errors and print the error code'''
    print("Error code:", e.code)
    sys.exit(1)
except urllib.error.URLError as e:
    '''This handle URL errors and print the reason'''
    print("URL Error:", e.reason)
    sys.exit(1)
except Exception as e:
    '''This handle other exceptions and print an error message'''
    print("Error:", e)
    sys.exit(1)
