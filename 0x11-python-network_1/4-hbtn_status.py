#!/usr/bin/python3
"""fetches http://0.0.0.0:5050/status using requests"""
import requests

if __name__ == "__main__":
    """fetches http://0.0.0.0:5050/status using requests"""
    r = requests.get('http://0.0.0.0:5050/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
