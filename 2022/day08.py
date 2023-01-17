
lines = open('day8.txt', 'r').readlines()
y_total = len(lines)
x_total = len(lines[0])
grid = [ []*x_total for i in range(y_total)]
for index, line  in enumerate(lines):
    line = line.strip()
    grid[index] = list(line)
#print(grid)

visible = []
captured = []
score = 0

def tag(address, tree):
    visible.append(tree)
    captured.append(address)

def check_visible(tree, position, row):
    if tree > max([x for x in row[0:position]]) or tree > max([x for x in row[position+1:]]):
        return True

def parta():
#ok first, make sure we can grab the edge items
    for x_axis, row in enumerate(grid):
        row = [eval(x) for x in row]
        #top and bottom
        if x_axis in [0, len(grid)-1]:
            visible.extend([x for x in row])
            for y in range(len(row)):
                captured.append(f'{x_axis}, {y}')
        for col_index, tree in enumerate(row):
            #left and right
            if col_index in [0, len(row)-1]:
                address = f'{x_axis}, {col_index}'
                if address not in captured:
                    tag(address, tree)
            else:
                address = f'{x_axis}, {col_index}'
                if address in captured:
                    continue
                if check_visible(tree, col_index, row):
                        tag(address, tree)
                else:
                    column = [eval(x[col_index]) for x in grid]
                    if check_visible(tree, x_axis, column):
                        tag(address, tree)

    print(len(visible))

def count(tree, row, to_reverse=None):
    if to_reverse:
        row.reverse()
    counter = 0
    for x in row:
        if x < tree:
            counter += 1
        if x >= tree:
            counter += 1
            break
    return counter

def trees_both(tree, position, row):
    return  count(tree, row[0:position], True) *  count(tree, row[position+1:])
#part b
for x_axis, row in enumerate(grid):
    #top and bottom
    if x_axis in [0, len(grid)-1]:
        continue
    row = [eval(x) for x in row]
    for col_index, tree in enumerate(row):
        #left and right
        if col_index in [0, len(row)-1]:
            continue
        #calculate num trees in each direction
        scenic = trees_both(tree, col_index, row)
        column = [eval(x[col_index]) for x in grid]
        scenic = scenic * trees_both(tree, x_axis, column)
        if scenic > score:
            score = scenic

print(score)

