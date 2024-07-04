#!/bin/bash
curl -s -o /tmp/body_response -w "%{http_code}" "$1"
[ "$(tail -n 1 /tmp/body_response)" = "200" ] && cat /tmp/body_response | head -n -1
