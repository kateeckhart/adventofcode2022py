#!/usr/bin/env python3

from common import *

class Monkey:
    def __init__(self, block):
        self.items = [int(x) for x in block[1][18:].split(',')]
        operator = block[2][23]
        arg = block[2][25:]
        if arg == 'old':
            if operator == '*':
                self.operator = lambda n: n**2
            else:
                self.operator = lambda n: n * 2
        else:
            arg_num = int(arg)
            if operator == '*':
                self.operator = lambda n: n * arg_num
            else:
                self.operator = lambda n: n + arg_num
        self.test = int(block[3][21:])
        self.true_throw = int(block[4][29:])
        self.false_throw = int(block[5][30:])
        self.inspect_count = 0

def calc_ans(input, rounds):
    monkies = [Monkey(x) for x in input]
    modulus = 1
    for monkey in monkies:
        modulus *= monkey.test
    for i in range(0, rounds):
        for monkey in monkies:
            for item in monkey.items:
                monkey.inspect_count += 1
                item = monkey.operator(item)
                if rounds == 20:
                    item //= 3
                item %= modulus
                if item % monkey.test == 0:
                    monkies[monkey.true_throw].items.append(item)
                else:
                    monkies[monkey.false_throw].items.append(item)
            monkey.items = []
    monkies.sort(key = lambda x: x.inspect_count, reverse = True)
    return monkies[0].inspect_count * monkies[1].inspect_count

def main():
    input = list_of_blocks(11)
    print_res(calc_ans(input, 20), calc_ans(input, 10000))

if __name__ == '__main__':
    main()
