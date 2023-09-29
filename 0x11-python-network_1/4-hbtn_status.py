#!/usr/bin/python3
"""
script that fetches url status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()

    '''Print the response body with tabulation'''
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

except requests.exceptions.RequestException as e:
    '''This handle requests exceptions'''
    print("Error:", e)
