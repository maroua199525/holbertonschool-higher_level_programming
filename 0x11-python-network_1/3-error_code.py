#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import urllib.request
import urllib.error
import sys


def send_error():
    """sends a request to the URL and displays the body of the response"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))

if __name__ == "__main__":
    send_error()