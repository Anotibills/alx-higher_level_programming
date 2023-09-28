#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response at once.
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1" || echo "Non-200 status code"

