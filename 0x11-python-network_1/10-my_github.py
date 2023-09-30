#!/usr/bin/python3
"""
script that takes your GitHub credentials
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = f"https://api.github.com/user"

    try:
        '''
        Send a GET request to the GitHub API using Basic Authentication.
        '''
        response = requests.get(url, auth=(username, personal_access_token))

        if response.status_code == 200:
            # If the request is successful, parse and display the user ID.
            user_info = response.json()
            print(user_info.get("id"))
        else:
            # If there is an error, print None.
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
