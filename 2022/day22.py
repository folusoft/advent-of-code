
import re
data = open('./day22.txt', 'r').read()
flat_map, instructions = data.split('\n\n')

##TODO need to figure out part 2

def create_map(flat_map):
    #print(len(list(flat_map.split('\n')[0])))
    longest_line = max([len(line) for line in flat_map.split('\n')])
    map = []
    for line in flat_map.split('\n'):
        if len(line) < longest_line:
            pad = ' ' * (longest_line - len(line))
            line = line + pad
        map.append(list(line))
    #print(f'rows: {len(map)}; cols: {len(map[0])}')
    return map

def get_starter(map):
    starter = None
    for rindex, row in enumerate(map):
        for cindex, col in enumerate(row):
            if map[rindex][cindex] == '.':
                starter = (rindex, cindex)
                break
        if starter:
            break
    return starter
def find_non_space(row, reverse:bool= False):
    if reverse:
        for index in range(len(row)-1, 0, -1):
            if row[index] != ' ':
                return index
    for index, item in enumerate(row):
        if item != ' ':
            return index
    assert False

def draw(map, direction, step, position):
    # print(f'moves starting from {position} {step} steps in {direction}')
    row = position[0]
    col = position[1]
    match direction:
        case '>':
            #we move increasingly along row (changing columns) until we run into a wall or space
            prior_col = col
            for count in range(step):
                print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
                if map[row][col] in ['.', '<', '>', '^', 'v']:
                    map[row][col] = direction
                prior_col = col
                col = (col + 1) % len(map[row])
                if map[row][col] == ' ':
                    col = find_non_space(map[row])
                if map[row][col] == '#':
                    col = prior_col
                    print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
                    break
        case '<':
            #we move decreasingly along row (changing columns) until we run into a wall or space
            prior_col = col
            for count in range(step):
                print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
                if map[row][col] in ['.', '<', '>', '^', 'v']:
                    map[row][col] = direction
                prior_col = col
                col = (col - 1) % len(map[row])
                if map[row][col] == ' ':
                    col = find_non_space(map[row], reverse=True)
                if map[row][col] == '#':
                    col = prior_col
                    print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
                    break
        case 'v':
            #move increasingly down column (changing rows)
            prior_row = row
            print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
            for count in range(step):
                if map[row][col] in ['.', '<', '>', '^', 'v']:
                    map[row][col] = direction
                prior_row = row
                row =  (row + 1) % len(map)
                if map[row][col] == ' ':
                    row = find_non_space([x[col] for x in map])
                if map[row][col] == '#':
                    row = prior_row
                    print(f'direction: {step}; {facing_score(direction)}, ({row}, {col})')
                    break
        case '^':
            prior_row = row
            #move increasingly up column (changing rows)
            for count in range(step):
                print(f'direction: {step}; {facing_score(direction)}, ({row}, {col}), {map[row][col]}')
                if map[row][col] in ['.', '<', '>', '^', 'v']:
                    map[row][col] = direction
                prior_row = row
                row =  (row - 1) % len(map)
                if map[row][col] == ' ':
                    row = find_non_space([x[col] for x in map], reverse=True)
                if map[row][col] == '#':
                    row = prior_row
                    print(f'stop: direction: {step}; {facing_score(direction)}, ({row}, {col})')
                    break
                
    return map, (row, col)

def printmap(map):
    for row in map:
        print(' '.join(row))

def get_direction(current, future):
    match current:
        case '>':
            if future == 'R':
                return 'v'
            return '^'
        case '<':
            if future == 'R':
                return '^'
            return 'v'
        case '^':
            if future == 'R':
                return '>'
            return '<'
        case 'v':   
            if future == 'R':
                return '<'
            return '>'  

def facing_score(direction):
    match direction:
        case '>':
            return 0
        case 'v':
            return 1
        case '<':
            return 2
        case '^':
            return 3
steps = [eval(num) for num in re.findall(r"\d+", instructions)]
directions = [dir for dir in list(instructions) if dir in ['R', 'L']]
assert len(steps) - len(directions) == 1

direction = '>'
map = create_map(flat_map)
position = get_starter(map)
# for count in range(149, 136, -1):
#     print(map[27][count], count)
for count, step in enumerate(steps):
    map, position = draw(map, direction, step, position)
    # print('final direction', position)
        #printmap(map)
    if count == len(directions):
        break
    direction = get_direction(direction, directions[count])
#printmap(map)
print(f'row: {position[0] + 1}, col: {position[1] + 1}, direction ({direction}): {facing_score(direction)} \n{1000 * (position[0]+1) + 4 * (position[1] + 1) + facing_score(direction)}')
