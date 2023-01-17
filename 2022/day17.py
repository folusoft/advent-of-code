import pandas as pd
import time
horiz = [(0,0), (0,1), (0,2), (0,3)]
plus = [(0,1), (1,0), (1,1), (1,2), (2,1)]
jay = [(0, 2), (1, 2), (2,0), (2,1), (2,2)]
vert = [(0,0), (1,0), (2,0), (3,0)]
sq = [(0,0), (0,1), (1,0), (1,1)]
directions = list(open('./day17.txt').read().strip())
rocks = [horiz, plus, jay, vert, sq]
chamber = []
chamber.insert(0, ['+', '-', '-', '-', '-', '-', '-', '-', '+'])
for count in range(4):
    chamber.insert(0, ['|', '.', '.', '.', '.', '.', '.', '.','|'])

#print(pd.DataFrame(chamber))
def move(rock, direction, chamber):
    #print(f'starting move to {direction} on {rock}')
    new = rock.copy()
    match direction:
        case '>':
             for index in range(len(new)):
                position = new[index]
                position = (position[0], (position[1] + 1))
                if chamber[position[0]][position[1]] == '#':
                    return rock
                new[index] = position
        case '<':
            for index in range(len(new)):
                position = new[index]
                position = (position[0], (position[1] - 1))
                if chamber[position[0]][position[1]] == '#':
                    return rock
                new[index] = position
    #test that right most edge is not touching the wall
    rightmost = max([x[1] for x in new])
    leftmost = min([x[1] for x in new])
    if leftmost < 1 or rightmost > 7:
        #print(f'decided not to move to {direction} on which would have been {new}')
        return rock
    #print(f'moving to {direction} on which is {new}')
    return new
    
def draw(chamber, rock, sign):
    for position in rock:
        chamber[position[0]][position[1]] = sign
    return chamber
bottom = len(chamber) - 1

#finds the last possible resting place for each position of the rock
def find_bottom(rock, chamber):
    bottoms = []
    for position in rock:
        hashes = [(index, position[1]) for index, row in enumerate(chamber) if row[position[1]] == '#']
        if len(hashes) > 0:
            top_most = min([x[0] for x in hashes if x[0] >= position[0]])
            bottoms.append((top_most-1, position[1]))
        else:
            bottoms.append((len(chamber)-2, position[1]))
    return bottoms

def find_top_rock(chamber):
    for row in range(len(chamber)):
        for col in range(1, 8, 1):
            if chamber[row][col] == '#':
                return (row, col)
    return (len(chamber)-1, 0)

def find_bottom_of_rock(rock):
    lowest_row = max([x[0] for x in rock])
    bottoms = [(x[0], x[1]) for x in rock if x[0] == lowest_row]
    return bottoms

def print_chamber_rocks(chamber):
    for index, row in enumerate(chamber):
        for col, cell in enumerate(row):
            if cell == '#':
                print((index, col))
#print(pd.DataFrame(chamber))

def get_chamber_length(chamber):
    top_hash = min([index for index, row in enumerate(chamber) if '#' in row])
    chamber_length = len(chamber)-top_hash-1
    return chamber_length

found = []
def debug_pattern(count, chamber, repeat_pattern):
    prior_pattern = ['|', '#', '#', '#', '.', '.', '#', '.', '|']
    #occurences = chamber.count(repeat_pattern)
    chamber_length = get_chamber_length(chamber)
    if chamber_length < 2752:
        return
    indices = [i for i, x in enumerate(chamber) if x == repeat_pattern]
    actual = [i for i in indices if chamber[i-1] == prior_pattern]
    if len(actual) > 0 and actual[0] == 19:
        print(f'at run: {count} and chamber length is {chamber_length} and repeat found at {actual}')
        #found.append(occurences)
            #print(pd.DataFrame(chamber).to_string())

def pattern_catcher(chamber, patterns):
    for pattern in chamber:
        if pattern.count('#') < 4:
            continue
        num_pattern = chamber.count(pattern)
        match num_pattern:
            case 4 | 5| 6:
                hashes = [x for x, content in enumerate(pattern) if content == '#']
                patterns.add("".join(str(e) for e in hashes))
    return patterns

direction_index = 0
patterns = set()

cols = [x for x in range(9)]

TOTAL_RUNS = 1000000000000
# values for sample
# RUNS_B4_PATTERN_STARTS = 38
# PATTERN_GENS_EVERY_RUN = 35
# PATTERN_HEIGHT = 53
# REPEAT_PATTERN = ['|', '.', '#', '#', '#', '#', '#', '#', '|']
# values for puzzle input
RUNS_B4_PATTERN_STARTS = 2449 #(or is it 2550)
PATTERN_GENS_EVERY_RUN = 1745
PATTERN_HEIGHT = 2752
REPEAT_PATTERN = ['|', '#', '#', '#', '.', '#', '#', '#', '|']
start = time.perf_counter()
base_height = 0
height_via_pattern = ((TOTAL_RUNS - RUNS_B4_PATTERN_STARTS) // PATTERN_GENS_EVERY_RUN) * PATTERN_HEIGHT
runs_to_get = (TOTAL_RUNS - RUNS_B4_PATTERN_STARTS) % PATTERN_GENS_EVERY_RUN
if runs_to_get == 0:
    runs_to_get = TOTAL_RUNS
runs = [x for x in range(RUNS_B4_PATTERN_STARTS)]
runs.extend([x for x in range(TOTAL_RUNS-runs_to_get, TOTAL_RUNS, 1)])

for count in runs:
    if count == RUNS_B4_PATTERN_STARTS and count != 0:
        #we have now started the repeating pattern
        base_height = get_chamber_length(chamber)
        #now we need to reset the chamber but with the pattern at the bottom
        chamber = []
        chamber.insert(0, REPEAT_PATTERN)
        chamber.append(['+', '-', '-', '-', '-', '-', '-', '-', '+'])
    #another attempt at catching patterns
    # patterns = pattern_catcher(chamber, patterns)
    # if count > 0:
    #     debug_pattern(count, chamber, REPEAT_PATTERN)
    drop_count, push_count = 0, 0
    #print(f'step {count+1} new rock at {count % len(rocks)} out of {len(rocks)} rocks falling with botton of {bottom}')
    rock = rocks[count % len(rocks)]
    highest_resting_rock = find_top_rock(chamber)[0]
    lowest_entering_rock = max([x[0] for x in rock])
    difference = (3 - (highest_resting_rock - lowest_entering_rock))
    #print(f'step {count+1}: highest resting rock {highest_resting_rock}, lowest entering rock {lowest_entering_rock}. New rows = 3 - {highest_resting_rock - lowest_entering_rock} = {difference}')
    if difference >= 0:
        for counter in range(difference + 1):
            chamber.insert(0, ['|', '.', '.', '.', '.', '.', '.', '.','|'])
    if difference < -1:
        for counter in range(difference +1, 0, 1):
            chamber.pop(0)
    #print_chamber_rocks(chamber)
    leftmost = min([x[1] for x in rock])
    for index in range(len(rock)):
        position = rock[index]
        position = (position[0], (position[1] + (3 - leftmost)))
        rock[index] = position
    chamber = draw(chamber, rock, '@')
    #print(pd.DataFrame(chamber))
    #now we move
    advance = True
    #print(f'starting: {rock}')
    while advance:
        #push
        direction = directions[direction_index % len(directions)]
        chamber = draw(chamber, rock, '.')
        rock = move(rock, direction, chamber)
        direction_index += 1
        push_count += 1
        #fall
        bottoms = find_bottom(rock, chamber)
        stop = [x[0] for index, x in enumerate(rock) if x[0] == bottoms[index][0]]
        if len(stop) > 0:
            advance = False
            #print(f'after {direction} and before down : {rock}, move: {advance}')
            break
        for index in range(len(rock)):
            position = rock[index]
            position = (position[0] + 1, position[1])
            rock[index] = position
        chamber = draw(chamber, rock, '#')
        drop_count += 1
        #print(f'after {direction} and down: {rock}, move: {advance}')
    #print(f'final: {rock}')
    chamber = draw(chamber, rock, '#')
    #print(pd.DataFrame(chamber))
    #print(f'step {count+1}: rock at {count % len(rocks)} out of {len(rocks)} rocks done after {push_count} pushes and {drop_count} drops. Next push is {direction_index}')

#print(pd.DataFrame(chamber).to_string())
chamber_height = get_chamber_length(chamber)
end = time.perf_counter()
print(f'after {TOTAL_RUNS}, chamber height: {chamber_height} + height from repeats: {height_via_pattern} = {height_via_pattern + chamber_height} and took {end - start:0.4f} seconds')

# possibles = open('./day17pp.txt').readlines()
# for possible in possibles:
#     print('***********************************************************************')
#     pattern = list(possible.strip())
#     indices = [x for x, content in enumerate(chamber) if content == pattern]
#     for index in indices:
#         print("########################################")
#         print(index-1, pd.DataFrame([chamber[index-1]]))
#         print(index, pd.DataFrame([chamber[index]]))

# for pattern in patterns:
#     pattern = [eval(x) for x in list(pattern)]
#     #create the hash pattern
#     row = ['|']
#     for col in cols:
#         if col == 0:
#             continue
#         if col == cols[-1]:
#             row.append('|')
#         elif col in pattern:
#             row.append('#')
#         else:
#             row.append('.')       
#     p_count = chamber.count(row)
#     print(pd.DataFrame([row]).to_string(), p_count)


   
        