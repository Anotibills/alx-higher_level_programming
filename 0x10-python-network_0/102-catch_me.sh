#!/bin/bash
# The script that makes a request to 0.0.0.0:5000/catch_me and captures the response.
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool" | grep -o "You got me!"


