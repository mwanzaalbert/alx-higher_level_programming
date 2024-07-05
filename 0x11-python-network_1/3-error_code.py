#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(body.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
