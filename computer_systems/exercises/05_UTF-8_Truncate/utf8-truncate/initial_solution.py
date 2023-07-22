import sys


def find_cutoff_point(line: bytes, trunc: int) -> int:
    if trunc <= 0 or trunc >= len(line):
        return trunc
    if (line[trunc] & 0xc0 == 0x80):
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
