raw_inp = open('input.txt', 'r')
inp = [[int(c) for c in line.strip()] for line in raw_inp]

class node():
    def __init__(self, _height, _position, gridsize):
        self.position = _position
        self.height = _height
        if _position[0]*_position[1] == 0 or _position[0] == gridsize[0]-1 or _position[1] == gridsize[1]-1:
            self.open = True
        else:
            self.open = False


class grid():
    def __init__(self, grid_values):
        self.gridsize = [len(grid_values), len(grid_values[0])]
        self.grid = [[node(grid_values[y][x], (x,y), self.gridsize) for x in range(len(grid_values[y]))] for y in range(len(grid_values))]
    def countOpenNodes(self):
        openNodes = 0
        for row in self.grid:
            for n in row:
                if n.open:
                    openNodes += 1
        return openNodes
    def generateOpenNodes(row):
        highestIndex = -1
        for n in row:
            if n.height > highestIndex:
                n.open = True
                highestIndex = n.height
    def generateAllOpenNodes(self):
        for row in self.grid:
            grid.generateOpenNodes(row)
            grid.generateOpenNodes(row[::-1])
        for column in [[self.grid[y][x] for y in range(len(self.grid))] for x in range(len(self.grid[0]))]:
            grid.generateOpenNodes(column)
            grid.generateOpenNodes(column[::-1])

def part1():
    gd = grid(inp)
    gd.generateAllOpenNodes()
    print(gd.countOpenNodes())

part1() #=>1803

class tree():
    def __init__(self, _height):
        self.height = _height
        self.neighbour = [None,None,None,None] #left, right, up, down
    def calculate_scenic_score(self):
        viewing_distances = [self.calculate_viewing_distance(self.height, 0), self.calculate_viewing_distance(self.height, 1), self.calculate_viewing_distance(self.height, 2), self.calculate_viewing_distance(self.height, 3)]
        return viewing_distances[0]*viewing_distances[1]*viewing_distances[2]*viewing_distances[3]
    def calculate_viewing_distance(self, height, direction):
        if self.neighbour[direction] != None:
            if self.neighbour[direction].height < height:
                return 1 + self.neighbour[direction].calculate_viewing_distance(height, direction)
            return 1
        return 0

def part2():
    forest = [[tree(n) for n in row] for row in inp]
    #print([[x.neighbour for x in r] for r in forest])
    for r in range(len(forest)):
        for c in range(len(forest[r])):
            #Add right & left neighbour
            if c > 0:
                forest[r][c].neighbour[0] = forest[r][c-1]
            if c < len(forest[r])-1:
                forest[r][c].neighbour[1] = forest[r][c+1]
            #Add up & down neighbour
            if r > 0:
                forest[r][c].neighbour[2] = forest[r-1][c]
            if r < len(forest)-1:
                forest[r][c].neighbour[3] = forest[r+1][c]

    scenic_scores = [[t.calculate_scenic_score() for t in r] for r in forest]
    print(scenic_scores[1])
    print(max([max(score_row) for score_row in scenic_scores]))

part2() #=>268912