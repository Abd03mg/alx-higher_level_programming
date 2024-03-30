#!/usr/bin/python3
""" script that takes a letter as argument and
sends a post request"""

if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) == 2 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        js = dict(eval(r.text))
        if (not js):
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except Exception:
        print("Not aa valid JSON")
