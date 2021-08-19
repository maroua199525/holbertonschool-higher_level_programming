#!/bin/bash
# a Bash script that sends a DELETE request to the URL
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
