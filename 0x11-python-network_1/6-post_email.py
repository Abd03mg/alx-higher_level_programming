#!/usr/bin/python3
""" Python script that Uses
'request' module to get X-Request-Id value."""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
