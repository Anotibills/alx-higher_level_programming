#!/bin/bash
# The script that sends a GET request to a URL and displays the body of a 200 status code response.
curl -s -I "$1" | grep -q "HTTP/1.1 200 OK" && curl -s "$1"

