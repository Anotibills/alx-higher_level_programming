#!/bin/bash
# script that sends a DELETE request to the URL passed as the first argument
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || { echo "I'm a DELETE request"; curl -X DELETE -s "$1"; }
#!/bin/bash
# This script displays a message, then sends a DELETE request to a URL and displays the body of the response.

[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || {curl -X DELETE -s "$1"; }
