#!/usr/bin/env python3

from common import *
from itertools import starmap

def parse_input():
    ret = []
    for line in list_of_lines(2):
        opponent = ord(line[0]) - ord('A')
        me = ord(line[2]) - ord('X')
        ret.append((opponent, me))
    return ret

# Stores which number (rps object) beats the one indexed
# e.g. Rock(0) == Paper(1) because rock is beatean by paper
beats_table = (1, 2, 0)

# Stores which number (rps object) is beated by the one indexed
# e.g. Rock(0) == Scissors(2) because rock is beats scissors
rev_beats_table = (2, 0, 1)

def play_round(op, me):
    if op == me:
        res = 3
    elif beats_table[op] == me:
        res = 6
    else:
        res = 0
    return res + me + 1

def play_round_part2(op, me):
    match me:
        case 0:
            return play_round(op, rev_beats_table[op])
        case 1:
            return play_round(op, op)
        case 2:
            return play_round(op, beats_table[op])

def main():
    input = parse_input()
    part1 = sum(starmap(play_round, input))
    part2 = sum(starmap(play_round_part2, input))
    print_res(part1, part2)

if __name__ == '__main__':
    main()
