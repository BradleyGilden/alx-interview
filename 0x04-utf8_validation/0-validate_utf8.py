#!/usr/bin/python3

"""
Author: Bradley Dillion Gilden
Date: 29-01-2024
"""


def validUTF8(data):
    """checks if int array is valid utf8, where each int represents a byte"""
    mask = 0xff
    # code point
    cp = 0

    for b in data:
        # prioritize lowest byte
        b = b & mask
        # ensure theres no code point greater than the 4byte like 1111 1---
        if (b & 0xf8 == 0xf8):
            return False
        # if showing 10-- ---- placeholder but no codepoint was set
        elif ((b & 0xc0 == 0x80) and (not cp)):
            return False
        # if showing 1,2,3 or 4 byte code point but the previous was not met
        elif ((not (b & 0xc0 == 0x80)) and cp):
            return False
        # set code point indicator to 4 bytes 1111 0---
        elif (b & 0xf8 == 0xf0):
            cp = 3
        elif (b & 0xf0 == 0xe0):
            cp = 2
        elif (b & 0xe0 == 0xc0):
            cp = 1
        elif (b & 0xc8 == 0x00):
            cp = 0

        if ((b & 0xc0 == 0x80) and cp):
            cp -= 1
    # if there are leftover places that were allocated
    if (cp):
        return False
    return True


if __name__ == '__main__':
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32,
            105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
