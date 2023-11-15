inp = open('input.txt', 'r')

def part1():
    #A, X: 'Rock' (+1); B, Y: 'Paper' (+2); C, Z: 'Scissors'(+3); Win +6, Draw +3, Loose +0
    lookup = {'A':{'X':1+3, 'Y':2+6, 'Z':3+0}, 'B':{'X':1+0, 'Y':2+3, 'Z':3+6}, 'C':{'X':1+6, 'Y':2+0, 'Z':3+3}}
    total_score = 0
    for line in inp:
        moves = line.strip().split(" ")
        try:
            total_score += lookup[moves[0]][moves[1]]
        except:
            print(moves)
    print(total_score)

def part2():
    #A: 'Rock'; B: 'Paper'; C: 'Scissors'; X: Loose; Y: Draw; Z: Win; Rock +1, Paper +2, Scissors +3; Win +6, Draw +3, Loose +0
    lookup = {'A':{'X':0+3, 'Y':3+1, 'Z':6+2}, 'B':{'X':0+1, 'Y':3+2, 'Z':6+3}, 'C':{'X':0+2, 'Y':3+3, 'Z':6+1}}
    total_score = 0
    for line in inp:
        moves = line.strip().split(" ")
        try:
            total_score += lookup[moves[0]][moves[1]]
        except:
            print(moves)
    print(total_score)

part2()