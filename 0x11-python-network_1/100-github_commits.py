#!/usr/bin/python3
"""

"""
import requests
import sys


def fetch_commits(owner, repo):
    '''
    This construct the URL for fetching commits
    '''
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"

    try:
        '''
        Send a GET request to the GitHub API to fetch the commits.
        '''
        response = requests.get(url)

        if response.status_code == 200:
            # If the request is successful, parse and print the commits.
            commits = response.json()
            for commit in commits:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {author_name}")
        else:
            '''
            If there is an error, print an error message with the status code.
            '''
            print("Failed to fetch commits. Status code:", end=" ")
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./fetch_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    '''This call the function to fetch and print commits.'''
    fetch_commits(owner_name, repo_name)
