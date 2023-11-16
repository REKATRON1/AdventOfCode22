raw_inp = open('input.txt', 'r')
inp = [[ord(x)-ord('a') for x in line.strip()] for line in raw_inp]
"""
'S -> -14', 'E -> -28'
"""
class node():
    def __init__(self, _height, _coordinates):
        self.height = _height
        self.coord = _coordinates
        self.isS = False
        self.prev = None
        self.open = False
    def path_length(self):
        if self.prev == None:
            return 0
        else:
            return 1 + self.prev.path_length()
    def get_neighbours(self, gridsize):
        neighbours = []
        if self.coord[0] != 0:
            neighbours.append([self.coord[0]-1, self.coord[1]])
        if self.coord[0] != gridsize[0]-1:
            neighbours.append([self.coord[0]+1, self.coord[1]])
        if self.coord[1] != 0:
            neighbours.append([self.coord[0], self.coord[1]-1])
        if self.coord[1] != gridsize[1]-1:
            neighbours.append([self.coord[0], self.coord[1]+1])
        return neighbours

def part1():
    grid = [[node(n, [y,x]) for x, n in enumerate(row)] for y, row in enumerate(inp)]
    gridsize = [len(grid), len(grid[0])]
    open_nodes = set()
    for row in grid:
        for n in row:
            if n.height == -14:
                n.height = 0
                n.open = True
                open_nodes.add(n)
            elif n.height == -28:
                n.height = ord('z')-ord('a')
                n.isS = True
    goal = None
    while len(open_nodes) > 0:
        new_open_nodes = set()
        for n in open_nodes:
            current_height = n.height
            for coord in n.get_neighbours(gridsize):
                neighbour = grid[coord[0]][coord[1]]
                if not neighbour.open and neighbour.height in list(range(current_height+2)):
                    neighbour.prev = n
                    neighbour.open = True
                    if neighbour.isS:
                        goal = neighbour
                        break
                    new_open_nodes.add(neighbour)
        open_nodes = new_open_nodes
    if goal == None:
        print('no path found')
    else:
        print(goal.path_length())

part1() #=>517

def part2():
    grid = [[node(n, [y,x]) for x, n in enumerate(row)] for y, row in enumerate(inp)]
    gridsize = [len(grid), len(grid[0])]
    open_nodes = set()
    for row in grid:
        for n in row:
            if n.height == -14 or n.height == 0:
                n.height = 0
                n.isS = True
            elif n.height == -28:
                n.height = ord('z')-ord('a')
                n.open = True
                open_nodes.add(n)
    goals = []
    while len(open_nodes) > 0:
        new_open_nodes = set()
        for n in open_nodes:
            current_height = n.height
            for coord in n.get_neighbours(gridsize):
                neighbour = grid[coord[0]][coord[1]]
                if not neighbour.open and neighbour.height in list(range(current_height-1, ord('z')-ord('a')+1)):
                    neighbour.prev = n
                    neighbour.open = True
                    if neighbour.isS:
                        goals.append(neighbour)
                    new_open_nodes.add(neighbour)
        open_nodes = new_open_nodes
    if len(goals) == 0:
        print('no path found')
    else:
        print(min([g.path_length() for g in goals]))

part2() #=>512