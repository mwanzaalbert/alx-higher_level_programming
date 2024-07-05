#!/usr/bin/python3
"""Send a request to a URL and prints its response or error code."""
import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Send a request to a URL and prints its response or error code."""
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    fetch_url(sys.argv[1])
