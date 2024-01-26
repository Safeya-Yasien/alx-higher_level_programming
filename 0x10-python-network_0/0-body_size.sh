#!/bin/bash
# Takes a URL, sends a request, and displays the size of the body of the response in bytes
# Usage: ./0-body_size.sh <URL>
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
