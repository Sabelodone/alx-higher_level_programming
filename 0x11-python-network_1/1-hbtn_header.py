#!/usr/bin/python3
"""A script that takes in a URL,
Sends a request to the URL,
And displays the value of the X-Request-Id
variable found in the header ofthe response.
"""

import sys
import urllib.request
from urllib.error import URLError

def get_request_id(url):
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            headers = dict(response.headers)
            request_id = headers.get("X-Request-Id")
            if request_id:
                print(f"The X-Request-Id value is: {request_id}")
            else:
                print("No X-Request-Id found in the response headers.")
    except URLError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        get_request_id(url)
