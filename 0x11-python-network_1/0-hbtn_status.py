#!/usr/bin/python3
"""Module to fetche https://intranet.hbtn.io/status"""
import urllib.request


def fetches_url():
    """function that fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))

if __name__ == "__main__":
    fetches_url()
