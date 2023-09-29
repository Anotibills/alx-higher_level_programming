#!/usr/bin/python3
"""
This script fetches the specified URL and displays the response.
"""
import urllib.request


def fetch_and_display(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()

            '''This print the response body'''
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode('utf-8')))

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_and_display(url)
