#!/bin/bash
# The script that sends a GET request to a URL and displays the body of a 200 status code response.
curl -s -w "%{http_code}" "$1" | awk 'END{if($1==200)system("tail -n +2")}'



