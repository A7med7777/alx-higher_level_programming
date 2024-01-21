#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    if num_args > 0:
        print(f"{num_args} argument:") if num_args == 1 else print(f"{num_args} arguments:")
        for i in range(num_args):
            print(f"{i + 1}: {args[i]}")
    else:
        print(f"0 arguments.")
