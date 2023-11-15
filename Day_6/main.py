raw_inp = open('input.txt', 'r')
inp = [line.strip() for line in raw_inp][0] #Only 1 Line Input

def part1():
    for pointer in range(len(inp)):
        interval = inp[pointer:pointer+4]
        int_dict = {x: True for x in interval}
        if len(list(int_dict.values())) == 4:
            print(pointer+4)
            return

part1() #=>1850

def part2():
    for pointer in range(len(inp)):
        interval = inp[pointer:pointer+14]
        int_dict = {x: True for x in interval}
        if len(list(int_dict.values())) == 14:
            print(pointer+14)
            return

part2() #=>2823