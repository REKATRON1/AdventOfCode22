raw_inp = open('input.txt', 'r')
inp = [line.strip() for line in raw_inp]

class stack():
    #newest element (idx 0) to oldest element
    content = []
    def __init__(self, _content):
        #_content[0]: newest element
        self.content = _content

    def push(self, items, inverted=True):
        #Items get inserted in the front of the stack
        new_content = []
        if inverted:
            new_content = items[::-1]
        else:
            new_content = items
        new_content.extend(self.content)
        self.content = new_content

    def top(self, amount=1):
        amount = min(amount, len(self.content))
        return self.content[:amount]

    def pop(self, amount=1):
        amount = min(amount, len(self.content))
        ret_content = self.content[:amount]
        new_content = self.content[amount:]
        self.content = new_content
        return ret_content

"""
initial stack arrangement
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""
str_stacks = ['CQB','ZWQR','VLRMB','WTVHZC','GVNBHZD','QVFJCPNH','SZWRTGD','PZWBNMGC','PFQWMBJN']
stacks = [stack([x for x in y]) for y in str_stacks]

def part1():
    try:
        moves = [(int(line.split(" ")[1]), int(line.split(" ")[3])-1, int(line.split(" ")[5])-1) for line in inp]
    except:
        return
    for move in moves:
        am, fr, to = move
        try:
            stacks[to].push(stacks[fr].pop(am))
        except:
            print([x.content for x in stacks])
            print(am, fr, to)
    sarr = [x.top() for x in stacks]
    top_str = ''
    for t in sarr:
        top_str += t[0]
    print(top_str)

part1() #=>BWNCQRMDB

def part2():
    try:
        moves = [(int(line.split(" ")[1]), int(line.split(" ")[3])-1, int(line.split(" ")[5])-1) for line in inp]
    except:
        return
    for move in moves:
        am, fr, to = move
        try:
            stacks[to].push(stacks[fr].pop(am), False)
        except:
            print([x.content for x in stacks])
            print(am, fr, to)
    sarr = [x.top() for x in stacks]
    top_str = ''
    for t in sarr:
        top_str += t[0]
    print(top_str)

part2() #=>NDPBQCLZP