#!/bin/bash
#  a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl --silent -X POST -H "Content-Type: application/json" "$1" --data @"$2"
