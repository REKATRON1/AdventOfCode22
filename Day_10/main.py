raw_inp = open('input.txt', 'r')
p_inp = [line.strip().split(' ') for line in raw_inp]
inp = []
for line in p_inp:
    if len(line) > 1:
        inp.append([line[0], int(line[1])])
    else:
        inp.append([line[0]])

def part1():
    interested_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strenght = 0
    register = 1
    current_cycle = 0
    for instruction in inp:
        current_cycle += 1
        if current_cycle in interested_cycles:
            total_signal_strenght += register * current_cycle
        if instruction[0] != 'noop':
            current_cycle += 1
            if current_cycle in interested_cycles:
                total_signal_strenght += register * current_cycle
            register += instruction[1]
    print(total_signal_strenght)

part1() #=>11780

def part2():
    register_values = [1] #inserting 1 element, so inx 1 is first element
    register = 1
    current_cycle = 0
    for instruction in inp:
        register_values.append(register)
        current_cycle += 1
        if instruction[0] != 'noop':
            register_values.append(register)
            current_cycle += 1
            register += instruction[1]
    image = []
    for phase in range(1, 240, 40):
        row = ''
        for idx in range(0, 40):
            if idx in [register_values[idx+phase]-1+x for x in range(3)]:
                row += '#'
            else:
                row += '.'
        image.append(row)

    for row in image:
        print(row)


part2() #=>
"""
###..####.#..#.#....###...##..#..#..##..
#..#....#.#..#.#....#..#.#..#.#..#.#..#.
#..#...#..#..#.#....###..#..#.#..#.#..#.
###...#...#..#.#....#..#.####.#..#.####.
#....#....#..#.#....#..#.#..#.#..#.#..#.
#....####..##..####.###..#..#..##..#..#.
"""