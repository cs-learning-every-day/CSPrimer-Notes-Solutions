import sys


def find_cutoff_point(line: bytes, first_byte: int) -> int:
    if first_byte == 0 or first_byte >= len(line):
        return first_byte
    cur = line[first_byte]
    prev = line[first_byte-1]
    if not is_unicode(cur):
        return first_byte
    if not is_unicode(prev):
        return first_byte
    return find_cutoff_point(line, first_byte - 1)


def truncate_unicode_line(line: bytes) -> bytes:
    first_byte, rest_of_line = line[0], line[1:]
    cutoff_point = find_cutoff_point(rest_of_line, first_byte)
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
