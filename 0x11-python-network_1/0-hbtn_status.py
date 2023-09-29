#!/usr/bin/python3
"""
Script that fetches url
"""
import urllib.request

'''Define the URL to fetch'''
url = "https://alx-intranet.hbtn.io/status"

try:
    '''Use 'urllib' to make an HTTP GET request to the URL'''
    with urllib.request.urlopen(url) as response:
        '''Read the response body as bytes'''
        html = response.read()

        '''This prints the response information with tabulation'''
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(repr(html)))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

except Exception as e:
    ''' This handle exceptions'''
    print("Error: {}".format(e))
