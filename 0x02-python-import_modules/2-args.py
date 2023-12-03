#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv) - 1
    print("{:d} {}".format(c, ("argument" if c == 1 else "arguments")), end='')
    print("{}".format("." if c == 0 else ":"))
    if c > 0:
        for i in range(0, c):
            print(i+1, ": {}".format(sys.argv[i+1]), sep='')
