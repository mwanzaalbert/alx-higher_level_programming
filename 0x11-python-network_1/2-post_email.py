#!/usr/bin/python3
"""Send a form data to a URL."""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """Send a form data to a URL."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
