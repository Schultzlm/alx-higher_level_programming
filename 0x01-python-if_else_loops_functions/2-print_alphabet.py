#!/usr/bin/python3
"""prints alphabet, in lowercase, not followed by a new line."""

for letter in range(97, 122):
    print("{}".format(chr(letter)), end="")
