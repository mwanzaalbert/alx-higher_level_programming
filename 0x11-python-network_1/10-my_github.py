#!/usr/bin/python3
"""Print the GitHub id of a user."""
import requests
import sys


def get_github_id(username, token):
    """Print the GitHub id of a user."""
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_id(username, token)
