raw_inp = open('input.txt', 'r')
inp = [line.strip() for line in raw_inp]

def part1():
    pair_ranges = [[line.split(',')[0].split('-'),line.split(',')[1].split('-')] for line in inp]
    fully_contained_counter = 0
    for pair in pair_ranges:
        try:
            lower_bound_dif = int(pair[0][0])-int(pair[1][0])
            upper_bound_dif = int(pair[0][1])-int(pair[1][1])
        except:
            print(pair)
            return
        if (lower_bound_dif <= 0 and upper_bound_dif >= 0) or (lower_bound_dif >= 0 and upper_bound_dif <= 0):
            fully_contained_counter += 1
    print(fully_contained_counter)

part1() #=>595

def part2():
    pair_ranges = [[line.split(',')[0].split('-'),line.split(',')[1].split('-')] for line in inp]
    overlap_counter = 0
    for pair in pair_ranges:
        try:
            lower_bounds = [int(pair[0][0]), int(pair[1][0])]
            upper_bounds = [int(pair[0][1]), int(pair[1][1])]
        except:
            print(pair)
            return
        if (lower_bounds[0] <= lower_bounds[1] and upper_bounds[0] >= lower_bounds[1]) or (lower_bounds[1] <= lower_bounds[0] and upper_bounds[1] >= lower_bounds[0]):
            overlap_counter += 1
    print(overlap_counter)

part2() #=>952