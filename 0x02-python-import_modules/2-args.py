#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    if num_args > 0:
        print("{num_args} argument:".format()) if num_args == 1 else print("{num_args} arguments:".format())
        for i in range(num_args):
            print("{i + 1}: {args[i]}".format())
    else:
        print("0 arguments.")
