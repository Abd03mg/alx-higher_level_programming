#!/usr/bin/python3
""" Python script that fetchs URL."""


from urllib import request

req = request.Request("https://alx-intranet.hbtn.io/status")
with request.urlopen(req) as res:
    con = res.read()
    print(
        'Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8'
        'content: {}'.format(type(con), con, con.decode("utf-8")))
