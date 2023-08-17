#!/usr/bin/env python3

from common import *

class DirEnt:
    def __init__(self, parent, name, size, is_file):
        self.parent = parent
        self.name = name
        self.children = dict()
        self.size = size
        self.is_file = is_file

    def calc_size(self):
        for child in self.children.values():
            child.calc_size()
            self.size += child.size

    def part1(self):
        ans = 0
        if self.size <= 100000 and not self.is_file:
            ans += self.size
        for child in self.children.values():
            ans += child.part1()
        return ans

    def part2(self, needed):
        ans = self.size
        if self.is_file or self.size < needed:
            return 70000000
        for child in self.children.values():
            ans = min(ans, child.part2(needed))
        return ans

def main():
    input = list_of_lines(7)
    root = DirEnt(None, '/', 0, False)
    curr_dir = root
    for line in input:
        input_parts = line.split(' ')
        if input_parts[0] == '$':
            if input_parts[1] == 'cd':
                match input_parts[2]:
                    case '/':
                        curr_dir = root
                    case '..':
                        curr_dir = curr_dir.parent
                    case _:
                        curr_dir = curr_dir.children[input_parts[2]]
        else:
            if input_parts[0] == 'dir':
                size = 0
            else:
                size = int(input_parts[0])
            curr_dir.children[input_parts[1]] = DirEnt(curr_dir, input_parts[1], size, input_parts[0] != 'dir')
    root.calc_size()
    part1 = root.part1()
    needed_space = root.size - 40000000
    part2 = root.part2(needed_space)
    print_res(part1, part2)

if __name__ == '__main__':
    main()
