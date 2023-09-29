#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
"""
import urllib.request
import urllib.parse
import sys

'''
This check if a URL and an email are provided as command-line arguments
'''
if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

'''Create a dictionary to store the email as a parameter'''
data = {'email': email}
data = urllib.parse.urlencode(data).encode('utf-8')

try:
    '''This Use 'urllib' to make a POST request to the provided URL'''
    with urllib.request.urlopen(url, data=data) as response:
        # Read the response body as bytes
        html = response.read()

        '''Print the decoded response content as a string (utf-8)'''
        print(html.decode('utf-8'))

except urllib.error.HTTPError as e:
    '''This handle HTTP errors'''
    print("Error code:", e.code)
    sys.exit(1)
except urllib.error.URLError as e:
    '''This handle URL errors'''
    print("URL Error:", e.reason)
    sys.exit(1)
except Exception as e:
    '''This handles any other exception'''
    print("Error:", e)
    sys.exit(1)
