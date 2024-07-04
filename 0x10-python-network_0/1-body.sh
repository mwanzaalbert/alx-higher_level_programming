#!/bin/bash
curl -s -X GET -L "$1" -o /tmp/body_response
cat /tmp/body_response
