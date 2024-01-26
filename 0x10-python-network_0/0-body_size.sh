#!/bin/bash
# This script sends a GET request to the provided URL and displays the size of the body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
