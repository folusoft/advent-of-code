import pandas as pd
lines = open('day14.txt', 'r').readlines()

map = []
smallest_x = 0
largest_x = 0
largest_y = 0

for line in lines:
    line = line.strip()
    coords = line.split('->')
    for index, coord in enumerate(coords):
        x, y = eval(coord.split(',')[0]), eval(coord.split(',')[1])
        if smallest_x:
            smallext_x =  min([x, smallest_x])
        else:
            smallest_x = x
        largest_x = max([x, largest_x])
        largest_y = max([y, largest_y])
#ok, build the map
map = [['.' for col in range(largest_x+1)] for row in range(largest_y + 1)]


#now populate map
for line in lines:
    line = line.strip()
    coordinates = line.split('->')
    for index, coord in enumerate(coordinates):
        x, y = eval(coord.split(',')[0]), eval(coord.split(',')[1])
        map[y][x] = '#'
        if index < len(coordinates) - 1:
            #grab the next coord
            next_coord = coordinates[index + 1]
            nx, ny = eval(next_coord.split(',')[0]), eval(next_coord.split(',')[1])
            if x != nx:
                #we are moving left or right
                for step in range(min([x, nx]), max([x, nx]) + 1):
                    map[y][step] = '#'
            if y != ny:
                #we are moving down
                for step in range(min([y, ny]), max([y, ny]) + 1):
                    map[step][x] = '#'

#now drop the sand
sand_entry = (0,500)
#we go down first then when blocked, left diag then right diag
abyss = False
units = 0
def part_a():
    while(not abyss):
        stop = False
        col = sand_entry[1]
        row = sand_entry[0]
        while(not stop and not abyss):
            if row >= len(map)-1:
                abyss = True
                stop = True
                break
            if map[row+1][col] == '.':
                #keep going down
                row = row + 1
            else:
                #check the left diag
                if map[row+1][col-1] == '.':
                    row += 1
                    col -= 1
                elif map[row+1][col+1] == '.':
                    row += 1
                    col += 1
                else:
                    stop = True
                    map[row][col] = 'o'
                #if we're here it means below us is a blocker
                #try diagonal
        units += 1

#part b
#first we add two more levels to the map
for count in range(2):
    if count == 0:
        map.append(['.' for col in range(largest_x+1)])
    else:
        map.append(['#' for col in range(largest_x+1)])

print(pd.DataFrame(map))
#print(len(map[0]), len(map))
#

blocked = False
while (not blocked):
    stop = False
    col = sand_entry[1]
    row = sand_entry[0]
    while(not stop):
        if col == len(map[0]) -1 :
            for index, map_row in enumerate(map):
                if index == len(map) - 1:
                     map[index].append('#')
                else:
                    map[index].append('.')
        if row == len(map)-2:
            stop = True
            map[row][col] = 'o'
            units += 1
            break
        #print(col, len(map[0]), row, len(map))
        if map[row+1][col] == '.':
            #keep going down
            row = row + 1
        else:
            #check the left diag
            if map[row+1][col-1] == '.':
                row += 1
                col -= 1
            elif map[row+1][col+1] == '.':
                row += 1
                col += 1
            else:
                #print(units, row, col)
                stop = True
                map[row][col] = 'o'
                units += 1
    #units += 1
    #print(pd.DataFrame(map))
    #at the end of everything, check if we've updated the row, col
    if row == sand_entry[0] and col == sand_entry[1]:
        blocked = True
    # if count >= 90:
    #     print(count, units, row, col)
   

print(pd.DataFrame(map))
print(stop, blocked)
print(units)

