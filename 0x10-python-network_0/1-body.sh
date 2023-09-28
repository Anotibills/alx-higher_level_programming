#!/bin/bash
# The script that sends a GET request to a URL and displays the body of a 200 status code response.
[ "$(curl -sI "$1" | grep -i '^HTTP' | grep -q ' 200')" ] && curl -s "$1"


