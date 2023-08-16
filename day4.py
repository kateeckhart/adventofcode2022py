#!/usr/bin/env python3

from common import *
import re

input_regex = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)$')

def main():
    input = list_of_lines(4)
    part1 = 0
    part2 = 0
    for line in input:
        parsed_line = input_regex.match(line)
        start1 = int(parsed_line[1])
        end1 = int(parsed_line[2])
        start2 = int(parsed_line[3])
        end2 = int(parsed_line[4])
        if start2 < start1 or (start1 == start2 and end1 < end2):
            tmp = start1
            start1 = start2
            start2 = tmp
            tmp = end1
            end1 = end2
            end2 = tmp
        if end1 >= end2:
            part1 += 1
        if end1 >= start2:
            part2 += 1
    print_res(part1, part2)

if __name__ == '__main__':
    main()
