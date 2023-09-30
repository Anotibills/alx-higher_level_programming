#!/usr/bin/python3
"""
This script takes in a URL and an email address
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    '''Define the data payload with the email parameter.'''
    data = {"email": email}

    try:
        response = requests.post(url, data=data)

        '''Check if the request was successful (status code 200).'''
        if response.status_code == 200:
            response_json = response.json()
            if "message" in response_json:
                print(response_json["message"])
            else:
                print("Response does not contain a 'message' field.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
