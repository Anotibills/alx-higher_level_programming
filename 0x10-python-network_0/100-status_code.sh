#!/bin/bash
# The script that sends a request to a URL passed as an argument,
curl -Is "$1" | awk 'NR==1{print $2}'

