#!/usr/bin/env python3

from common import *

def main():
    input = block_of_int(1)
    elves = sorted(map(sum, input), reverse = True)
    part2 = elves[0] + elves[1] + elves[2]
    print_res(elves[0], part2)

if __name__ == '__main__':
    main()
