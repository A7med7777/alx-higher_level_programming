#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = 98
    result += a ** b

dis.dis(magic_calculation)
