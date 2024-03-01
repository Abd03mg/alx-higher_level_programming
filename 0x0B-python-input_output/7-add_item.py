#!/usr/bin/python3
''' LOAD, ADD, SAVE '''


if __name__ == "__main__":
    json = __import__("json")
    argv = __import__("sys").argv
    try:
        with open("add_item.json", "w+", encoding="utf-8") as f:
            item = list(json.load(f))
            print(item)
            except json.decoder.JSONDecodeError:
            item = []
            item += argv[1:]
            json.dump(item, f)
