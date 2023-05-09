#!/usr/bin/python3
eye = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - eye)), end="")
    eye = 32 if eye == 0 else 0
