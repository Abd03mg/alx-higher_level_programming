#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    su = 0
    c = len(sys.argv) - 1
    for i in range(0, c):
        su += int(sys.argv[i+1])
    print("{:d}".format(su))
