#!/usr/bin/env python3

from common import *

def calc_ans(input, has_floor):
    grid = [[0 for x in range(0, 1000)] for x in range(0, 1000)]
    for line in input:
        paths = [tuple(int(cord) for cord in path.split(',')) for path in line.split('->')]
        from_x = paths[0][0]
        from_y = paths[0][1]
        for to_x, to_y in paths[1:]:
            while from_y != to_y or from_x != to_x:
                grid[from_y][from_x] = 1
                from_x += sgn(to_x - from_x)
                from_y += sgn(to_y - from_y)
            grid[from_y][from_x] = 1

    if has_floor:
        lowest_y = 0
        for y, row in enumerate(grid):
            for tile in row:
                if tile != 0:
                    lowest_y = y
        for x in range(0, len(grid[0])):
            grid[lowest_y + 2][x] = 1

    while True:
        sand_x = 500
        sand_y = 0
        while sand_y + 1 < len(grid) or grid[0][500] != 0:
            if grid[sand_y + 1][sand_x] == 0:
                sand_y += 1
            elif grid[sand_y + 1][sand_x - 1] == 0:
                sand_y += 1
                sand_x -= 1
            elif grid[sand_y + 1][sand_x + 1] == 0:
                sand_y += 1
                sand_x += 1
            else:
                grid[sand_y][sand_x] = 2
                break
        if sand_y + 1 >= len(grid) or grid[0][500] != 0:
            break

    ans = 0
    for row in grid:
        for tile in row:
            if tile == 2:
                ans += 1
    return ans

def main():
    input = list_of_lines(14)

    print_res(calc_ans(input, False), calc_ans(input, True))

if __name__ == '__main__':
    main()
