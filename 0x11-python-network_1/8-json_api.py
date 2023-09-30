#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        # Send a POST request to the URL with the data payload.
        response = requests.post(url, data=data)

        '''
        Check if the response body is properly JSON formatted and not empty.
        '''
        if response.headers.get("content-type") == "application/json":
            user_info = response.json()
            if "id" in user_info and "name" in user_info:
                # If JSON contains 'id' and 'name', display the result.
                print(f"[{user_info['id']}] {user_info['name']}")
            else:
                # If JSON is not in the expected format, display "No result."
                print("No result")
        else:
            # If JSON is not properly formatted, display "No result."
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
