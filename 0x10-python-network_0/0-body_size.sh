#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL
curl -s -I "$1" | grep "Content-Length" | cut -f2 -d:
