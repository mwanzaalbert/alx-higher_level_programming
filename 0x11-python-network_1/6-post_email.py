#!/usr/bin/python3
"""Send a form data to a URL."""
import requests
import sys


def post_email(url, email):
    """Send a form data to a URL."""
    response = requests.post(url, data={'email': email})
    print(response.text)
    # print(f"Your email is: {response.text}")


if __name__ == "__main__":
    post_email(sys.argv[1], sys.argv[2])
