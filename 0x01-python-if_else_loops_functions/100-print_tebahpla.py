#!/usr/bin/python3
print_tebahpla = ""
for char_code in range(ord('z'), ord('a') - 1, -1):
    if char_code % 2 == 0:
        print_tebahpla += chr(char_code)
    else:
        print_tebahpla += chr(char_code).upper()
print("{}".format(print_tebahpla))

