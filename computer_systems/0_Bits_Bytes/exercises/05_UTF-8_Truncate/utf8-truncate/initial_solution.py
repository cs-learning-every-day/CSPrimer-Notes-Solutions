import sys


def find_cutoff_point(line: bytes, trunc: int) -> int:
    if trunc >= len(line):
        return trunc
    ## Why are the two conditions below not equivalent for all values?
    ## It is true that all unicode characters will be larger than 128
    ## But we are only interested in setting our pointer backwards
    ## if we have landed at a continuation byte
    ## A starting byte (that indicates length of utf-8 encoding)
    ## Will also be > 128, but for these we don't necessarily want to 
    ## continue truncating
    ## A decimal alternative would be x > 128 and x < 191
    ##                                x > 0xC0 and x < 0xef
    if not (line[trunc] & 0xc0 == 0x80) and (line[trunc] > 128):
        pass
    #if (line[trunc] & 0xc0 == 0x80):
    if (line[trunc] > 128 and line[trunc] <= 191):
        return find_cutoff_point(line, trunc - 1)
    return trunc


def truncate_unicode_line(line: bytes) -> bytes:
    first_byte, rest_of_line = line[0], line[1:]
    cutoff_point = find_cutoff_point(rest_of_line[:-1], first_byte)
    truncated_line = rest_of_line[:cutoff_point]
    if truncated_line != rest_of_line and rest_of_line[-1] == 10:
        truncated_line += b'\n'
    return truncated_line


def is_unicode(i: int) -> bool:
    return i > 128


file = sys.argv[1]
with open(file, 'rb') as f:
    while f.peek():
        sys.stdout.buffer.write(truncate_unicode_line(f.readline()))
