raw_inp = open('input.txt', 'r')
p_inp = [line.strip() for line in raw_inp]

def process_input(p_inp):
    inp = []
    inp_pair = []
    for line in p_inp:
        if line == '' and len(inp_pair) == 2:
            inp.append(inp_pair)
            inp_pair = []
        else:
            content = []
            layer = -1
            for x in line.split(','):
                s, pot_int = False, ''
                for i, n in enumerate(x):
                    if n == '[':
                        if layer != -1:
                            get_layer(content, layer).append([])
                        layer += 1
                    elif n == ']':
                        if s:
                            get_layer(content, layer).append(int(pot_int))
                            s, pot_int = False, ''
                        layer -= 1
                    else:
                        s = True
                        pot_int += n
                if s:
                    get_layer(content, layer).append(int(pot_int))
            inp_pair.append(content)
    if len(inp_pair) == 2:
        inp.append(inp_pair)
    return inp

def get_layer(content, layer):
    if layer == 0:
        return content
    else:
        return get_layer(content[-1], layer-1)

inp = process_input(p_inp)

def part1():
    indices = []
    for i, pair in enumerate(inp):
        ret = part1_rec(pair[0], pair[1])
        if ret:
            indices.append(i+1)
    print(sum(indices))

def part1_rec(l1, l2):
    if type(l1) == list and type(l2) == int:
        l2 = [l2]
    elif type(l1) == int and type(l2) == list:
        l1 = [l1]
    for i in range(len(l1)):
        if i == len(l2):
            return False
        if type(l1[i]) == list or type(l2[i]) == list:
            ret = part1_rec(l1[i], l2[i])
            if ret != None:
                return ret
        elif l1[i] < l2[i]:
            return True
        elif l1[i] > l2[i]:
            return False
    if len(l1) == len(l2):
        return None
    return True

part1() #=>5682

def convpart1(a, b):
    k = part1_rec(a, b)
    if k == None:
        return 0
    if k:
        return -1
    else:
        return 1

import functools

def part2():
    new_inp = []
    for pair in inp:
        new_inp.extend(pair)
    l, h = [[2]], [[6]]
    new_inp.extend([l, h])
    new_inp.sort(key=functools.cmp_to_key(convpart1))
    print((new_inp.index(l)+1)*(1+new_inp.index(h)))

part2() #=>20304