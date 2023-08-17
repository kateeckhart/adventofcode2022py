#!/usr/bin/env python3

from common import *

def main():
    input = list_of_lines(10)
    ins_iter = iter(input)
    x = 1
    next_x = 1
    wait = False
    signal_strength = 0
    rastor_image = [[' ' for x in range(0, 40)] for x in range(0, 6)]
    for cycle in range(0, 240):
        rastor_x = cycle % 40
        rastor_y = cycle // 40
        if rastor_x == 19 and rastor_y <= 5:
            signal_strength += (cycle + 1) * x
        if x >= rastor_x - 1 and x <= rastor_x + 1:
            rastor_image[rastor_y][rastor_x] = '#'

        if not wait:
            ins = next(ins_iter)
            ins_parts = ins.split(' ')
            if ins_parts[0] == 'addx':
                next_x = x + int(ins_parts[1])
                wait = True
        else:
            x = next_x
            wait = False
    part2 = '\n' + '\n'.join(map(lambda x: ''.join(x), rastor_image));
    print_res(signal_strength, part2)

if __name__ == '__main__':
    main()
