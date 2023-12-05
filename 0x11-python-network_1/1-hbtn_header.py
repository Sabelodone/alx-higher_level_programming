mport sys
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
