#!/usr/bin/python3
"""Module to take in a URL, send a request to the URL """
import urllib.request
import sys


def send_url():
    """that sends a request to the URL and displays the value """
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])

if __name__ == "__main__":
    send_url()
