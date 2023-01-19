import pandas as pd
import math
lines = open('day09.txt', 'r').readlines()

#starting over
NUM_KNOTS = 10
knots = [(0,0) for i in range(NUM_KNOTS)]
moves = {'R' : (1, 0), 'L' : (-1, 0), 'U' : (0, 1), 'D' : (0, -1)}

def print_array(chamber):
    mrow = len(chamber) - 1
    while mrow >= 0:
        print(str(chamber[mrow]).replace(',', '').replace("'", ""))
        mrow += -1

def print_knots():
    knots.append((0,0))
    print(knots)
    cols = 1 + max([x[0] for x in knots]) - min([x[0] for x in knots])
    rows = 1 + max([x[1] for x in knots]) - min(x[1] for x in knots)
    c_pad = 0
    if min([x[0] for x in knots]) < 0:
        c_pad = abs(min([x[0] for x in knots]))
    r_pad = 0
    if min(x[1] for x in knots) < 0:
        r_pad = abs(min(x[1] for x in knots))
    chamber = [['.' for x in range(cols+c_pad+1)] for y in range(rows+r_pad+1)]
    for index, position in enumerate(knots):
        col = position[0] + c_pad
        row = position[1] + r_pad
        if index == 0:
            chamber[row][col] = f'H'
        elif index == len(knots) - 1:
             chamber[row][col] = f'S'
        elif index == len(knots) - 2:
             chamber[row][col] = f'T'
        else:
            chamber[row][col] = f'{str(index)}'
    print_array(chamber)

#last entry is the tail
visits = set()

def get_eight_positions(p):
    return [p, (p[0] - 1, p[1]), (p[0] + 1, p[1]), (p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] - 1, p[1] - 1), (p[0] + 1, p[1] + 1), (p[0] + 1, p[1] - 1)]

def touching(t_coord, h_coord):
    #build the 8 positions around the 
    all_positions = get_eight_positions(t_coord)
    return h_coord in all_positions

def move_head(direction, front):
    increment = moves.get(direction)
    front = (front[0] + increment[0], front[1] + increment[1])
    return front

def move_tail(T, H, match=(0,0)):
    #move rule is if head is ever 2 steps directly up/down/left/right then move in that direction
    #check up down to see if difference is more than 1
    adder = 1
    if abs(T[1] - H[1]) > 1 and T[0] == H[0]:
        adder = int(math.copysign(adder, H[1] - T[1]))
        T = (T[0], T[1] + adder)
    elif abs(T[0] - H[0]) > 1 and T[1] == H[1]:
        adder = int(math.copysign(adder, H[0] - T[0]))
        T = (T[0] + adder, T[1])
    else:
        #if you're above me check L/R
        if H[1] > T[1]:
            #check L/R
            if H[0] < T[0]:
                #above and to the left, move diag left
                T = (T[0] - 1, T[1] + 1)
            elif H[0] > T[0]:
                #above and to the right, move diag right
                T = (T[0] + 1, T[1] + 1)
            else:
                T = (T[0], T[1] + 1)
        else:
            if H[0] < T[0]:
                #below and to the left, move diag left
                T = (T[0] - 1, T[1] - 1)
            elif H[0] > T[0]:
                #above and to the right, move diag right
                T = (T[0] + 1, T[1] - 1)
            else:
                T = (T[0], T[1] - 1)
    return T
fail = False
for number, line in enumerate(lines):
    if fail:
        break
    line = line.strip()
    direction = line.split()[0]
    units = eval(line.split()[1])
    #R, L is x axis and U, D is y axis
    for unit in range(units):
        knots[0] =  move_head(direction, knots[0])
        for index in range(1, len(knots), 1):
            H = knots[index-1]
            T = knots[index]
            # if direction == 'U':
            #     print(f' for unit {unit+1} out of {units} current index: {index} is at {T} while prior is at {H} they are touching: {touching(T, H)}')
            if not touching(T, H):
                match direction:
                    case 'R':
                        knots[index] = move_tail(T, H, (1, 0))
                    case 'L':
                        knots[index] = move_tail(T, H, (-1, 0))
                    case 'U':
                        knots[index] = move_tail(T, H, (0, 1))
                    case 'D':
                        knots[index] = move_tail(T, H, (0, -1))
            #now ensure it's still touching
            if not touching(knots[index], H):
                print(f'What?? {index}, {T}->{knots[index]} and {index-1}, {knots[index-1]} are not touching after {unit} in {direction} direction on line {number}')
                fail = True
            # if direction == 'U':
            #     print(f' after unit {unit+1} out of {units} current index: {index} is at {knots[index]} while prior is at {H}')
        # print_knots()  
        # print()
        visits.add(knots[len(knots) - 1]) 
    # print("#########################################")
         

print(len(visits))
#print(knots)
#print(visits)
#print_knots()
