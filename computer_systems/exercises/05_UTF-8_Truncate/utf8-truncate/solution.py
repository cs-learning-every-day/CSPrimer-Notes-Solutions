import os
import sys
import re
import pdb

OUTPUT_FILE = 'output'

if OUTPUT_FILE in os.listdir():
    os.remove(OUTPUT_FILE)

output_file = open(OUTPUT_FILE, 'wb')

with open('cases', 'rb') as f:
    while f.peek():
        line = f.readline()
        first_byte, rest_of_line = line[0], line[1:]
        cutoff_point = first_byte
        if cutoff_point <= len(rest_of_line):
            while rest_of_line[cutoff_point-1] > 128 and cutoff_point > 0:
                cutoff_point -= 1
        truncated_line = rest_of_line[:cutoff_point]
        if truncated_line != rest_of_line:
            truncated_line += b'\n'
        output_file.write(truncated_line)


output_file.close()

