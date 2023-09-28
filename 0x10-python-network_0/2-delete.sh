#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument
curl -s -X DELETE "$1" || { echo "Usage: $0 <URL>"; exit 1; }

