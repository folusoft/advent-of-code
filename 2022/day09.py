import pandas as pd
lines = open('day09.txt', 'r').readlines()

##TODO need to figure out part 2

#starting over
NUM_KNOTS = 10
knots = [(0,0) for i in range(NUM_KNOTS)]
moves = {'R' : (1, 0), 'L' : (-1, 0), 'U' : (0, 1), 'D' : (0, -1)}
#last entry is the tail
visits = set()
visits.add((0,0))
def touching(t_coord, h_coord, direction):
    #this is touching if T is next to or adjacent to H
    #check left or right
    tx, ty = t_coord[0], t_coord[1]
    hx, hy = h_coord[0], h_coord[1]
    #look left/right, up/down, diag left/diag right 
    ok_dist = [0, 1]
    match direction:
        case 'R' | 'L':
            #print(t_coord, h_coord)
            #the head moved up, so check up and diagonal
            if abs(hx-tx) in ok_dist or (abs(hx-tx) in ok_dist and abs(hy-ty) in ok_dist):
                return True
        case 'U' | 'D':
            #print(t_coord, h_coord)
            if abs(hy-ty) in ok_dist or (abs(hx-tx) in ok_dist and abs(hy-ty) in ok_dist):
                return True
    return False

def move(direction, front):
    increment = moves.get(direction)
    front = (front[0] + increment[0], front[1] + increment[1])
    return front

for line in lines:
    line = line.strip()
    direction = line.split()[0]
    units = eval(line.split()[1])
    #R, L is x axis and U, D is y axis
    for unit in range(units):
        knots[0] =  move(direction, knots[0])
        for index in range(1, len(knots), 1):
            H = knots[index-1]
            T = knots[index]
            # if direction == 'U' and index == 5:
            #     print(f' for unit {unit+1} out of {units} current index: {index} is at {T} while prior is at {H}')
            match direction:
                case 'R':
                    if not touching(T, H, direction):
                        if T[1] == H[1]:
                            T = (T[0] + 1, T[1])
                        else:
                            T = (T[0] + 1, H[1])
                        knots[index] = T
                        if index == len(knots) - 1:
                            visits.add(T)
                    # print(T, H)
                case 'L':
                    if not touching(T, H, direction):
                        if T[1] == H[1]:
                            T = (T[0]-1, T[1])
                        else:
                            T = (T[0] - 1, H[1])
                        knots[index] = T
                        if index == len(knots) - 1:
                            visits.add(T)
                    # print(T, H)
                case 'U':
                    if not touching(T, H, direction):
                        #print("change")
                        if T[0] == H[0]:
                            T = (T[0], T[1] + 1)
                        else:
                            T = (H[0], T[1] + 1)
                        knots[index] = T
                        if index == len(knots) - 1:
                            visits.add(T)
                    # print(T, H)
                case 'D':
                    if not touching(T, H, direction):
                        if T[0] == H[0]:
                            T = (T[0], T[1] - 1)
                        else:
                            T = (H[0], T[1] - 1)
                        knots[index] = T
                        if index == len(knots) - 1:
                            visits.add(T)
                    # print(T, H)

print(len(visits))
