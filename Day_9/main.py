raw_inp = open('input.txt', 'r')
inp = [[line.strip().split(' ')[0], int(line.strip().split(' ')[1])] for line in raw_inp]

#L, R, U, D -> [0, -1], [0, 1], [-1, 0], [1, 0]
move_translate = {'L': [0, -1], 'R':[0, 1], 'U':[-1, 0], 'D':[1, 0]}

class grid():
    def __init__(self, initial_size=[501, 501], start_pos=[250, 250]):
        self.grid = [[False for x in range(initial_size[1])] for y in range(initial_size[0])]
        self.grid[start_pos[0]][start_pos[1]]=True
        self.head = [start_pos[0], start_pos[1]]
        self.tail = [start_pos[0], start_pos[1]]
    def move(self, direction, amount):
        for x in range(amount):
            self.head[0] += direction[0]
            self.head[1] += direction[1]
            self.update_tail()
    def update_tail(self):
        if abs(self.head[0]-self.tail[0]) > 2 or abs(self.head[1]-self.tail[1]) > 2:
            print('error')
        if abs(self.head[0]-self.tail[0]) > 1:
            if self.head[0]-self.tail[0] > 0:
                self.tail[0] += 1
            else:
                self.tail[0] -= 1
            if abs(self.head[1]-self.tail[1]) == 1:
                self.tail[1] = self.head[1]
        elif abs(self.head[1]-self.tail[1]) > 1:
            if abs(self.head[0]-self.tail[0]) == 1:
                self.tail[0] = self.head[0]
            if self.head[1]-self.tail[1] > 0:
                self.tail[1] += 1
            else:
                self.tail[1] -= 1
        self.grid[self.tail[0]][self.tail[1]] = True
    def count_visited_spots(self):
        counter = 0
        for row in self.grid:
            for x in row:
                if x:
                    counter += 1
        return counter

def part1():
    move_list = [[move_translate[move[0]], move[1]] for move in inp]
    gd = grid([291, 181], [171, 120])
    for move in move_list:
        gd.move(move[0], move[1])
    print(gd.count_visited_spots())

part1() #=>6037


class grid2():
    def __init__(self, length=10, initial_size=[501, 501], start_pos=[250, 250]):
        self.grid = [[False for x in range(initial_size[1])] for y in range(initial_size[0])]
        self.grid[start_pos[0]][start_pos[1]]=True
        self.rope = [[start_pos[0], start_pos[1]] for x in range(length)]
    def move(self, direction, amount):
        for x in range(amount):
            self.rope[0][0] += direction[0]
            self.rope[0][1] += direction[1]
            for t in range(len(self.rope)):
                self.update_tail(t)
            self.grid[self.rope[-1][0]][self.rope[-1][1]] = True
    def update_tail(self, t):
        if t == 0:
            return
        head, tail = self.rope[t-1], self.rope[t]
        if abs(head[0]-tail[0]) > 2 or abs(head[1]-tail[1]) > 2:
            print('error')
        elif abs(head[0]-tail[0]) == 2 and abs(head[1]-tail[1]) == 2:
            if head[0]-tail[0] > 0:
                tail[0] += 1
            else:
                tail[0] -= 1
            if head[1]-tail[1] > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
        elif abs(head[0]-tail[0]) > 1:
            if head[0]-tail[0] > 0:
                tail[0] += 1
            else:
                tail[0] -= 1
            if abs(head[1]-tail[1]) == 1:
                tail[1] = head[1]
        elif abs(head[1]-tail[1]) > 1:
            if abs(head[0]-tail[0]) == 1:
                tail[0] = head[0]
            if head[1]-tail[1] > 0:
                tail[1] += 1
            else:
                tail[1] -= 1
    def count_visited_spots(self):
        counter = 0
        for row in self.grid:
            for x in row:
                if x:
                    counter += 1
        return counter

def part2():
    move_list = [[move_translate[move[0]], move[1]] for move in inp]
    gd = grid2(10, [291, 181], [171, 120])
    for move in move_list:
        gd.move(move[0], move[1])
    print(gd.count_visited_spots())

part2() #=>2485