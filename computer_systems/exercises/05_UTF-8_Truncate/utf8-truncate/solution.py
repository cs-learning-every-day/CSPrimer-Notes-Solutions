"""
- Parse Test cases
    - Read Lines
    - uint8 for n
    - remember to strip trailing \n
- Truncation
    - Start from end
    - if s[n] starts with 0b10 then n -=1
    - Remember to account for n out of bounds
- Finally
    - Print to standard out
    - Diff against expected
"""
import sys


def truncate(string: bytes, num: int) -> bytes:
    if num >= len(string):
        return string
    import pdb;pdb.set_trace()
    # If byte at trunation piont starts with 10 specifically then we move pointer down
    # Finding if byte starts with 10
        # Mask out the first two bits - by bitwise and on 0b11000000 (or 0xC0)
        # Check if they are equivalent to 0b10000000 (or 0x80)
    while num > 0 & (string[num] & 0xc0 == 0x80):
        num -= 1
    return string[:num]


with open('cases', 'rb') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        n = line[0]
        s = line[1:-1]
        res = truncate(s, n)
        sys.stdout.buffer.write(res + b'\n')

