#!/bin/bash
# The script that takes in a URL, sends a POST request to the passed URL
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
