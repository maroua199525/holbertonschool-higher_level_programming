#!/usr/bin/python3
"""sends a request to the URL and displays the value of X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id", None))
