raw_inp = open('input.txt', 'r')
inp = [line.strip() for line in raw_inp]

letter_lookup = {chr(i):i-ord('a')+1 for i in range(ord('a'), ord('z')+1)}
for i in range(ord('A'), ord('Z')+1):
    letter_lookup[chr(i)]=i-ord('A')+27


def part1():
    backpacks = [[line[:int(len(line)/2)],line[int(len(line)/2):]] for line in inp]
    score = 0
    for bp in backpacks:
        bp1 = {x:True for x in bp[0]}
        added = False
        for x in bp[1]:
            if bp1.get(x) != None:
                score += letter_lookup[x]
                added = True
                break
        if not added:
            print("Error at Backpack:", bp)
    print(score)

part1() #=>7553

def part2():
    if len(inp)%3 != 0:
        print("Cannot group into triples without leftover")
        return
    groups = [[inp[3*i], inp[3*i+1], inp[3*i+2]] for i in range(int(len(inp)/3))]
    score = 0
    for group in groups:
        bp1 = {x:False for x in group[0]}
        added = False
        for x in group[1]:
            if bp1.get(x) != None:
                bp1[x] = True
        for y in group[2]:
            if bp1.get(y) != None and bp1[y]:
                score += letter_lookup[y]
                added = True
                break
        if not added:
            print("Error at Group:", group)
    print(score)

part2() #=>2758