#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || { echo "I'm a DELETE request"; curl -X DELETE -s "$1"; }

