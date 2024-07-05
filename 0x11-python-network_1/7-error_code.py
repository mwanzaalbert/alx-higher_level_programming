#!/usr/bin/python3
"""Send a request to a URL and prints its response or error code."""
import requests
import sys


def fetch_url(url):
    """Send a request to a URL and prints its response or error code."""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url(sys.argv[1])
