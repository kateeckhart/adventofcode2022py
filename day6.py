#!/usr/bin/env python3

from common import *

def calc_ans(input, size):
    for i in range(0, len(input) - size):
        letters = set(input[i: i + size])
        if len(letters) == size:
            return i + size

def main():
    input = read_input(6)
    part1 = calc_ans(input, 4)
    part2 = calc_ans(input, 14)
    print_res(part1, part2)

if __name__ == '__main__':
    main()
