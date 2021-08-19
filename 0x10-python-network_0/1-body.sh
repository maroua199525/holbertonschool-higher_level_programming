#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL
curl -s -L -X GET "$1"
