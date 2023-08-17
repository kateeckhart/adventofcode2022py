#!/usr/bin/env python3

from common import *
import re

ins_regex = re.compile(r'^move (\d+) from (\d+) to (\d+)$')

def parse_crates(crates_input):
    crates = [[] for x in range(0, len(crates_input[0]))]
    for line in crates_input:
        for (i, item) in enumerate(line):
            if item != ' ':
                crates[i].append(item)
    return crates

def calc_ans(crates_input, instructions, is_part2):
    crates = parse_crates(crates_input)
    for ins in instructions:
        ins_match = ins_regex.match(ins)
        count = int(ins_match[1])
        fom = int(ins_match[2]) - 1
        to = int(ins_match[3]) - 1
        crane_arm = crates[fom][-count:]
        del crates[fom][-count:]
        if not is_part2:
            crane_arm.reverse()
        crates[to] += crane_arm
    return ''.join(map(lambda x: x[-1], crates))

def main():
    input = list_of_blocks(5)
    crates_input = [x[1::4] for x in input[0][:-1]]
    crates_input.reverse()
    instructions = input[1]

    part1 = calc_ans(crates_input, instructions, False)
    part2 = calc_ans(crates_input, instructions, True)
    print_res(part1, part2)

if __name__ == '__main__':
    main()
