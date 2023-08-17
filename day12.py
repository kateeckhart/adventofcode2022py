#!/usr/bin/env python3

from common import *
import heapq

def main():
    input = list_of_lines(12)
    elevation_grid = [[0 for x in range(0, len(input[0]))] for x in range(0, len(input))]
    start_x = -1
    start_y = -1
    goal_x = -1
    goal_y = -1

    for y, line in enumerate(input):
        for x, square in enumerate(line):
            if square == 'S':
                elevation_grid[y][x] = 0
                start_x = x
                start_y = y
            elif square == 'E':
                elevation_grid[y][x] = 25
                goal_x = x
                goal_y = y
            else:
                elevation_grid[y][x] = ord(square) - ord('a')
    distance_grid = [[999999999 for x in range(0, len(input[0]))] for x in range(0, len(input))]
    queue = [(0, goal_y, goal_x)]

    while len(queue) > 0:
        distance, y, x = heapq.heappop(queue)
        if distance_grid[y][x] <= distance:
            continue
        distance_grid[y][x] = distance
        elevation = elevation_grid[y][x]
        for y_offset, x_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            adj_y = y + y_offset
            adj_x = x + x_offset
            if adj_y < 0 or adj_y >= len(elevation_grid) or adj_x < 0 or adj_x >= len(elevation_grid[0]):
                continue
            adj_elevation = elevation_grid[adj_y][adj_x]
            adj_distance = distance_grid[adj_y][adj_x]
            if adj_distance < distance + 1 or adj_elevation < elevation - 1:
                continue
            heapq.heappush(queue, (distance + 1, adj_y, adj_x))
    part1 = distance_grid[start_y][start_x]
    part2 = 99999999999
    for ele_line, dis_line in zip(elevation_grid, distance_grid):
        for elevation, distance in zip(ele_line, dis_line):
            if elevation == 0:
                part2 = min(part2, distance)
    print_res(part1, part2)

if __name__ == '__main__':
    main()
