#!/usr/bin/python3
from urllib import request
url = "https://youtube.com"
response = request.urlopen(url)
print(response)