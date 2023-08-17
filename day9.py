#!/usr/bin/env python3

from common import *

def sgn(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

def calc_ans(input, knot_count):
    rope_xs = [0 for i in range(0, knot_count)]
    rope_ys = [0 for i in range(0, knot_count)]
    seen = set()
    for line in input:
        line_parts = line.split(' ')
        dir = line_parts[0]
        distance = int(line_parts[1])
        for _ in range(0, distance):
            match dir:
                case 'L':
                    rope_xs[0] -= 1
                case 'R':
                    rope_xs[0] += 1
                case 'U':
                    rope_ys[0] += 1
                case 'D':
                    rope_ys[0] -= 1
            for i in range(1, knot_count):
                column_diff = rope_xs[i - 1] - rope_xs[i]
                row_diff = rope_ys[i - 1] - rope_ys[i]
                if abs(row_diff) > 1 or abs(column_diff) > 1:
                    rope_ys[i] += sgn(row_diff)
                    rope_xs[i] += sgn(column_diff)
            seen.add((rope_xs[-1], rope_ys[-1]))
    return len(seen)

def main():
    input = list_of_lines(9)
    print_res(calc_ans(input, 2), calc_ans(input, 10))

if __name__ == '__main__':
    main()
