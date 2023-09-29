#!/usr/bin/python3
"""
Script that fetches url"""
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

        try:
            '''Attempt to decode the content using UTF-8'''
            content = html.decode('utf-8')
            print("\t- content:", content)
        except UnicodeDecodeError:
            print("\t- content: Unable to decode as UTF-8")

except Exception as e:
    '''Handle exceptions, if any'''
    print(e)
