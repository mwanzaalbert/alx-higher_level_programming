#!/bin/bash
# This script makes a request to cause the server to respond with "You got me!"
curl -s -X PUT -L -d "user_id=98" "http://0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool"
