#!/usr/bin/python3
""" Python script that Uses
'request' module to fetch URl."""

if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}"
          "\n\t- content: {}".format(type(r.text), r.text))
