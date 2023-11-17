raw_inp = open('input.txt', 'r')
p_inp = [line.strip() for line in raw_inp]

def process_input(p_inp):
    rock_lines = []
    for line in p_inp:
        p_line = line.split('->')
        coords = [[int(x) for x in p_coord.split(',')] for p_coord in p_line]
        for x in range(len(coords)-1):
            new_rock_line = [coords[x], coords[x+1]]
            rock_lines.append(new_rock_line)

    max_indices = [max(rock_lines, key=lambda x: x[1][0])[1][0], max(rock_lines, key=lambda x: x[1][1])[1][1]]
    min_indices = [min(rock_lines, key=lambda x: x[0][0])[0][0], min(rock_lines, key=lambda x: x[0][1])[0][1]]
    #In the imput the y coord is [1] and x coord is [0]: max_index for y coord bcs sand drops from 0 500
    grid_size = [max_indices[0]-min_indices[0],max_indices[1]][::-1]
    #Add 1 left and right so last sand can fall of screen and add 1 on bottom so if sand gets to last layer its an indication that it falls of screen
    grid_size = [grid_size[0]+2, grid_size[1]+3]
    x_conv = min_indices[0]-1
    #y_conv is 0

    grid = [[0 for x in range(grid_size[1])] for y in range(grid_size[0])]
    #Set Sand-Spawner
    spawner_point = [0, 500-x_conv]
    grid[spawner_point[0]][spawner_point[1]] = 100

    for rock_line in rock_lines:
        start, end = rock_line[0], rock_line[1]
        if start[0] == end[0]:
            iterator = 1
            if start[1] > end[1]:
                iterator = -1
            for y in range(start[1], end[1]+iterator, iterator):
                grid[y][start[0]-x_conv] = 1
        else:
            iterator = 1
            if start[0] > end[0]:
                iterator = -1
            for x in range(start[0], end[0]+iterator, iterator):
                grid[start[1]][x-x_conv] = 1
    return grid, x_conv

def part1():
    grid, x_conv = process_input(p_inp)
    dropped_sand = 0
    sand_off_screen = False
    spawner_point = [0, 500-x_conv]
    while not sand_off_screen:
        if grid[spawner_point[0]][spawner_point[1]] != 100:
            #Overfill
            sand_off_screen = True
            print('Overfill')
        else:
            new_sand = spawner_point.copy()
            landed = False
            while not landed:
                if new_sand[0] == len(grid)-1:
                    landed = True
                    sand_off_screen = True
                    print('Sand off screen')
                else:
                    current_ground = grid[new_sand[0]+1][new_sand[1]]
                    #No Problem with subtracting or adding to x-coord bcs outer edges of grid is clear
                    diag_ground_left, diag_ground_right = grid[new_sand[0]+1][new_sand[1]-1], grid[new_sand[0]+1][new_sand[1]+1]
                    if current_ground == 0:
                        #falling 1 down
                        new_sand[0] += 1
                    elif current_ground == 1 or current_ground == 2:
                        if diag_ground_left == 0:
                            #falling diag left
                            new_sand = [new_sand[0]+1, new_sand[1]-1]
                        elif diag_ground_right == 0:
                            #falling diag right
                            new_sand = [new_sand[0]+1, new_sand[1]+1]
                        else:
                            #landed on sand or stone
                            grid[new_sand[0]][new_sand[1]] = 2
                            dropped_sand += 1
                            landed = True
                    else:
                        print('unknown ground', current_ground)
    print(dropped_sand)

part1() #=>832

def process_input2(p_inp):
    rock_lines = []
    for line in p_inp:
        p_line = line.split('->')
        coords = [[int(x) for x in p_coord.split(',')] for p_coord in p_line]
        for x in range(len(coords)-1):
            new_rock_line = [coords[x], coords[x+1]]
            rock_lines.append(new_rock_line)

    max_indices = [max(rock_lines, key=lambda x: x[1][0])[1][0], max(rock_lines, key=lambda x: x[1][1])[1][1]]
    min_indices = [min(rock_lines, key=lambda x: x[0][0])[0][0], min(rock_lines, key=lambda x: x[0][1])[0][1]]
    #In the imput the y coord is [1] and x coord is [0]: max_index for y coord bcs sand drops from 0 500
    grid_size = [max_indices[0]-min_indices[0],max_indices[1]][::-1]
    #max possible witdh from spawner would be 2*height (+2) and add 1 on bottom so if sand gets to last layer its an indication that it falls of screen
    grid_size = [grid_size[0]+3, grid_size[1]+3]
    grid_size[1] = max(grid_size[1], grid_size[0]*2+3)
    #center 0 500:
    x_conv = -(int(grid_size[0])+1-500)
    #y_conv is 0

    grid = [[0 for x in range(grid_size[1])] for y in range(grid_size[0])]
    #Set Sand-Spawner
    spawner_point = [0, 500-x_conv]
    grid[spawner_point[0]][spawner_point[1]] = 100

    for rock_line in rock_lines:
        start, end = rock_line[0], rock_line[1]
        if start[0] == end[0]:
            iterator = 1
            if start[1] > end[1]:
                iterator = -1
            for y in range(start[1], end[1]+iterator, iterator):
                grid[y][start[0]-x_conv] = 1
        else:
            iterator = 1
            if start[0] > end[0]:
                iterator = -1
            for x in range(start[0], end[0]+iterator, iterator):
                grid[start[1]][x-x_conv] = 1
    for x in range(len(grid[-1])):
        grid[-1][x] = 1
    return grid, x_conv

def part2():
    grid, x_conv = process_input2(p_inp)
    dropped_sand = 0
    sand_off_screen = False
    spawner_point = [0, 500-x_conv]
    while not sand_off_screen:
        if grid[spawner_point[0]][spawner_point[1]] != 100:
            #Overfill
            sand_off_screen = True
        else:
            new_sand = spawner_point.copy()
            landed = False
            while not landed:
                current_ground = grid[new_sand[0]+1][new_sand[1]]
                #No Problem with subtracting or adding to x-coord bcs outer edges of grid is clear
                diag_ground_left, diag_ground_right = grid[new_sand[0]+1][new_sand[1]-1], grid[new_sand[0]+1][new_sand[1]+1]
                if current_ground == 0:
                    #falling 1 down
                    new_sand[0] += 1
                elif current_ground == 1 or current_ground == 2:
                    if diag_ground_left == 0:
                        #falling diag left
                        new_sand = [new_sand[0]+1, new_sand[1]-1]
                    elif diag_ground_right == 0:
                        #falling diag right
                        new_sand = [new_sand[0]+1, new_sand[1]+1]
                    else:
                        #landed on sand or stone
                        grid[new_sand[0]][new_sand[1]] = 2
                        dropped_sand += 1
                        landed = True
                else:
                    print('unknown ground', current_ground)
    print(dropped_sand)

part2() #=>27601