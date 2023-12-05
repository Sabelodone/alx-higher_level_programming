#!/usr/bin/python3
"""This script fetches data from
    https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error fetching data: {}".format(e.reason))

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_data(url)
