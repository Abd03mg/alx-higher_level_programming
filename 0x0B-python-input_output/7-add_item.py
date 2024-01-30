#!/usr/bin/python3
''' LOAD, ADD, SAVE '''


if __name__ == "__main__":
    json = __import__("json")
    argv = __import__("sys").argv
    isfile = __import__("os").path.isfile

    with open("add_item.json", "a+", encoding="utf-8") as f:
        if (json.load(f)):
            item = list(json.load(f))
        else:
            item = []

        for i in range(len(argv)):
            item.append(argv[i])
        json.dump(item, f)
