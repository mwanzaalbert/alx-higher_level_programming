#!/usr/bin/python3
"""Fetch a header of a response from a URL."""
import requests
import sys


def fetch_x_request_id(url):
    """Fetch a header of a response from a URL."""
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found")


if __name__ == "__main__":
    fetch_x_request_id(sys.argv[1])
