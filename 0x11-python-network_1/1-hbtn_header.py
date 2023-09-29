#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL, and displays the value
"""
import urllib.request


def fetch_and_display_x_request_id(url):
    try:
        """
        Use 'urllib' to make an HTTP GET request to the provided URL
        """
        with urllib.request.urlopen(url) as response:
            # Retrieve the headers from the response
            headers = response.info()

            # Search for the 'X-Request-Id' header and print its value
            x_request_id = headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in response headers.")

    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io"
    fetch_and_display_x_request_id(url)
