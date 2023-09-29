#!/usr/bin/python3
"""
script that fetches url
"""
import urllib.request

'''Define the URL to fetch'''
url = "https://alx-intranet.hbtn.io/status"

try:
    '''Use 'urllib.request.urlopen' to make an HTTP GET request to the URL'''
    with urllib.request.urlopen(url) as response:
        html = response.read()
        
        '''Print the response information with tabulation'''
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html.decode('utf-8'))
except Exception as e:
    # Handle exceptions, if any
    print(e)

