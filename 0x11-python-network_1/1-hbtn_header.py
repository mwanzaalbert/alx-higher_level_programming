#!/usr/bin/python3
"""Fetch a header of a response from a URL."""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Making the request and handling the response
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Fetching the value of X-Request-Id header
        x_request_id = response.getheader('X-Request-Id')

        if x_request_id:
            print(x_request_id)
