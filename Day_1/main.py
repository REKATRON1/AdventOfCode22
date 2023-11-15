inp = open('input.txt', 'r')

def part1():
    elfes = []
    new_elf = 0
    most_carried = 0
    for count, line in enumerate(inp):
        if line.strip() == "":
           elfes.append(new_elf)
           if new_elf > most_carried:
                most_carried = new_elf
           new_elf = 0
        else:
            try:
                new_elf +=  int(line.strip())
            except:
               print(line.strip())
    if new_elf != 0:
        elfes.append(new_elf)
        if new_elf > most_carried:
           most_carried = new_elf

    print(most_carried)

def part2():
    elfes = []
    new_elf = 0
    top_carried = [0, 0, 0]
    for count, line in enumerate(inp):
        if line.strip() == "":
           elfes.append(new_elf)
           if new_elf > top_carried[0]:
                top_carried[0] = new_elf
                top_carried = sorted(top_carried)
           new_elf = 0
        else:
            try:
                new_elf += int(line.strip())
            except:
               print(line.strip())
    if new_elf != 0:
       elfes.append(new_elf)
       if new_elf > top_carried[0]:
            top_carried[0] = new_elf
            top_carried = sorted(top_carried)

    print(top_carried, sum(top_carried))

part2()