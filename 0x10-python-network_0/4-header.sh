#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL with header variable
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
