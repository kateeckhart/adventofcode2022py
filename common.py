def read_input(day):
    with open(f'input/day{day}.txt', mode='rt', encoding='UTF-8') as f:
        return f.read().strip()

def list_of_blocks(day):
    return [block.split('\n') for block in read_input(day).split('\n\n')]

def list_of_lines(day):
    return read_input(day).split('\n')

def list_of_int(day):
    return [int(line) for line in list_of_lines(day)]

def block_of_int(day):
    return [[int(line) for line in block] for block in list_of_blocks(day)]

def grid_of_int(day):
    return [[int(digit) for digit in line] for line in list_of_lines(day)]

def print_res(part1, part2 = None):
    print(f'Part 1 is {part1}')
    if part2 is not None:
        print(f'Part 2 is {part2}')
