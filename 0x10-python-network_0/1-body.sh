#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for status code 200
curl -s -o /tmp/body_response -w "%{http_code}" "$1" | grep -q 200 && cat /tmp/body_response
