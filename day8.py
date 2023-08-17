#!/usr/bin/env python3

from common import *

def tree_scan_p1(forest, mark_vis, start_y, start_x, step_y, step_x):
    biggest = -1
    y = start_y
    x = start_x
    while y >= 0 and y < len(forest) and x >= 0 and x < len(forest[0]):
        tree = forest[y][x]
        if biggest < tree:
            mark_vis(y, x)
        biggest = max(tree, biggest)
        y += step_y
        x += step_x

def tree_scan_p2(forest, mark_vis, start_y, start_x, step_y, step_x):
    y = start_y + step_y
    x = start_x + step_x

    my_tree = forest[start_y][start_x]
    while y >= 0 and y < len(forest) and x >= 0 and x < len(forest[0]):
        tree = forest[y][x]
        mark_vis()
        if my_tree <= tree:
            break
        y += step_y
        x += step_x

def main():
    input = grid_of_int(8)
    vis_flag = [[False for x in row] for row in input]
    def mark_vis_p1(y, x):
        vis_flag[y][x] = True
    for y in range(0, len(input)):
        tree_scan_p1(input, mark_vis_p1, y, 0, 0, 1)
        tree_scan_p1(input, mark_vis_p1, y, len(input[0]) - 1, 0, -1)
    for x in range(0, len(input[0])):
        tree_scan_p1(input, mark_vis_p1, 0, x, 1, 0)
        tree_scan_p1(input, mark_vis_p1, len(input) - 1, x, -1, 0)

    part1 = 0
    for row in vis_flag:
        for tree in row:
            if tree:
                part1 += 1

    part2 = 0
    for i in range(0, len(input)):
        for j in range(0, len(input[0])):
            scenic = 1
            for step_y, step_x in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                next_scenic = [0]
                def mark_vis_p2():
                    next_scenic[0] += 1
                tree_scan_p2(input, mark_vis_p2, i, j, step_y, step_x)
                scenic *= next_scenic[0]
            part2 = max(part2, scenic)

    print_res(part1, part2)

if __name__ == '__main__':
    main()
