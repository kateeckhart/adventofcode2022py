#!/usr/bin/env python3

from common import *
import functools

def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    elif item >= 'A' and item <= 'Z':
        return ord(item) - ord('A') + 27 

def main():
    input = list_of_lines(3)
    part1 = 0
    for line in input:
        half = len(line) // 2
        compart1 = set(line[:half])
        compart2 = set(line[half:])
        part1 += priority((compart1 & compart2).pop())
    part2 = 0
    for i in range(0, len(input), 3):
        group = [set(x) for x in input[i:i + 3]]
        part2 += priority(functools.reduce(lambda x, y: x & y, group).pop())
    print_res(part1, part2)

if __name__ == '__main__':
    main()
