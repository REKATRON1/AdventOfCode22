import math

raw_inp = open('input.txt', 'r')
p_inp = [line.strip().split(' ') for line in raw_inp]

class monkey():
    def __init__(self, starting_items, _operation, testing):
        self.items = starting_items
        self.operation = _operation
        self.test = testing

        self.inspect_counter = 0
    def apply_operation(self):
        new_items = []
        for item in self.items:
            self.inspect_counter += 1
            new_item = item
            if self.operation[0] == '+':
                new_item += self.operation[1]
            elif self.operation[0] == '*':
                new_item *= self.operation[1]
            else:
                new_item *= new_item
            new_items.append(math.floor(new_item/3))
        self.items = new_items
    def apply_test(self):
        if self.items[0] % self.test[0] == 0:
            return self.test[1]
        else:
            return self.test[2]
    def throw_item(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item
    def get_item(self, item):
        self.items.append(item)

monkeys = []
s = 0
for l, inp in enumerate(p_inp):
    if inp[0] == 'Monkey':
        new_stats = []
        s = l
    elif l-s == 1:
        items = []
        x = False
        for i, item in enumerate(inp):
            if x:
                items.append(int(item.split(',')[0]))
            else:
                if item == 'items:':
                    x = True
        new_stats.append(items)
    elif l-s == 2:
        if inp[-1] == 'old':
            new_stats.append(['', 0])
        else:
            new_stats.append([inp[-2], int(inp[-1])])
    elif l-s == 3:
        new_stats.append([int(inp[-1])])
    elif l-s == 4 or l-s == 5:
        new_stats[-1].append(int(inp[-1]))
    elif l-s == 6:
        monkeys.append(monkey(new_stats[0], new_stats[1], new_stats[2]))

def part1():
    for i in range(20):
        for monkey in monkeys:
            monkey.apply_operation()
            for x in range(len(monkey.items)):
                monkeys[monkey.apply_test()].get_item(monkey.throw_item())
    print(sorted([monkey.inspect_counter for monkey in monkeys])[-1]*sorted([monkey.inspect_counter for monkey in monkeys])[-2])

part1() #=>62_491

class monkey2():
    def __init__(self, starting_items, _operation, testing):
        self.items = starting_items
        self.operation = _operation
        self.test = testing

        self.inspect_counter = 0
    def apply_operation(self):
        new_items = []
        for item in self.items:
            self.inspect_counter += 1
            new_item = item
            if self.operation[0] == '+':
                for m in range(len(new_item)):
                    new_item[m][0] += self.operation[1]
                    new_item[m][0] = new_item[m][0] % new_item[m][1]
            elif self.operation[0] == '*':
                for m in range(len(new_item)):
                    new_item[m][0] *= self.operation[1]
                    new_item[m][0] = new_item[m][0] % new_item[m][1]
            else:
                for m in range(len(new_item)):
                    new_item[m][0] *= new_item[m][0]
                    new_item[m][0] = new_item[m][0] % new_item[m][1]
            new_items.append(new_item)
        self.items = new_items
    def apply_test(self):
        for m in self.items[0]:
            if m[1] == self.test[0]:
                if m[0] == 0:
                    return self.test[1]
                break
        return self.test[2]
    def throw_item(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item
    def get_item(self, item):
        self.items.append(item)

relevant_mods = {}
for inp in p_inp:
    if inp[0] == 'Test:':
        m = int(inp[-1])
        if relevant_mods.get(m) == None:
            relevant_mods[m] = True
relevant_mods = list(relevant_mods.keys())

monkeys = []
s = 0
for l, inp in enumerate(p_inp):
    if inp[0] == 'Monkey':
        new_stats = []
        s = l
    elif l-s == 1:
        items = []
        x = False
        for i, item in enumerate(inp):
            if x:
                items.append([[int(item.split(',')[0]) % m, m] for m in relevant_mods])
            else:
                if item == 'items:':
                    x = True
        new_stats.append(items)
    elif l-s == 2:
        if inp[-1] == 'old':
            new_stats.append(['', 0])
        else:
            new_stats.append([inp[-2], int(inp[-1])])
    elif l-s == 3:
        new_stats.append([int(inp[-1])])
    elif l-s == 4 or l-s == 5:
        new_stats[-1].append(int(inp[-1]))
    elif l-s == 6:
        monkeys.append(monkey2(new_stats[0], new_stats[1], new_stats[2]))

def part2():
    for i in range(10000):
        for monkey in monkeys:
            monkey.apply_operation()
            for x in range(len(monkey.items)):
                monkeys[monkey.apply_test()].get_item(monkey.throw_item())
    print(sorted([monkey.inspect_counter for monkey in monkeys])[-1]*sorted([monkey.inspect_counter for monkey in monkeys])[-2])

part2() #=>17_408_399_184