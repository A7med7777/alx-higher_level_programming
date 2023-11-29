#!/usr/bin/python3
for i in range(99):
    first = i / 10
    last = i % 10
    print("{:d}{:d}".format(int(first), int(last)), end=", ")
print(99)
