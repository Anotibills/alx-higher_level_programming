#!/bin/bash
# The script that sends a request to a URL passed as an argument
(curl -Is "$1" | grep -i "^HTTP" | awk '{print $2}' && exit) || exit 1
