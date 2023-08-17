#!/usr/bin/env python3

from common import *
import functools

@functools.total_ordering
class PacketKey:
    def __init__(self, inner):
        if not isinstance(inner, int) and not isinstance(inner, list):
            raise TypeError('Packet sort only supported by list and int')
        self.inner = inner

    def __eq__(self, rhs):
        return self is rhs or (isinstance(rhs, PacketKey) and self.inner == rhs.inner)

    def __lt__(self, rhs):
        if not isinstance(rhs, PacketKey):
            raise TypeError()
        elif isinstance(self.inner, int) and isinstance(rhs.inner, int):
            return self.inner < rhs.inner
        elif isinstance(self.inner, list) and isinstance(rhs.inner, list):
            lhs_iter = iter(self.inner)
            rhs_iter = iter(rhs.inner)
            while True:
                try:
                    rhs_val = PacketKey(next(rhs_iter))
                except StopIteration:
                    return False
                try:
                    lhs_val = PacketKey(next(lhs_iter))
                except StopIteration:
                    return True
                if lhs_val != rhs_val:
                    return lhs_val < rhs_val
        elif isinstance(self.inner, list) and isinstance(rhs.inner, int):
            return self < PacketKey([rhs.inner])
        else:
            return PacketKey([self.inner]) < rhs

def main():
    input = list_of_lines(13)
    packets = []
    for line in input:
        if line.strip() == '':
            continue
        packets.append(eval(line))

    part1 = 0
    for i in range(0, len(packets), 2):
        if PacketKey(packets[i]) < PacketKey(packets[i + 1]):
            part1 += (i // 2) + 1
    packets += [[[2]], [[6]]]
    packets.sort(key = PacketKey)
    part2 = 1
    for i, packet in enumerate(packets, 1):
        if packet == [[2]] or packet == [[6]]:
            part2 *= i
    print_res(part1, part2)

if __name__ == '__main__':
    main()
