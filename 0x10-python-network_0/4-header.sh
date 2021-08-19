#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL with header variable
curl -s -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"