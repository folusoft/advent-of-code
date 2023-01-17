import pandas as pd
lines = open('./day23.txt', 'r').readlines()
elves = []
cols = len(list(lines[0].strip()))
rows = len(lines)
pad = 2

##TODO need to figure out part 2

def printmap(positions):
    #get max cols, 
    dcols = max([x[1] for x in positions]) + pad * 4
    drows = max([x[0] for x in positions]) + pad * 4
    map = [['.' for x in range(dcols)] for row in range(drows)]
    for position in positions:
        map[position[0] + pad ][position[1] + pad] = '#'
    print(pd.DataFrame(map))
#gets the positions
for row, line in enumerate(lines):
    line = line.strip()
    elves.extend([(row, index) for index, x in enumerate(list(line)) if x == '#'])
#show positions
#print(elves)
#ok let's try to print the map
tests = [{'step': 'N', 'tests' : ['N', 'NE', 'NW']},
             {'step': 'S', 'tests' : ['S', 'SE', 'SW']},  
             {'step': 'W', 'tests' : ['W', 'NW', 'SW']}, 
             {'step': 'E', 'tests' : ['E', 'NE', 'SE']},
            ]
def no_elves(elf):
    #check 8 positions around the elf, if we don't have any elves, we return True
    all_positions = [(elf[0] - 1, elf[1]), (elf[0] + 1, elf[1]), (elf[0], elf[1] - 1), (elf[0], elf[1] + 1), (elf[0] - 1, elf[1] + 1), (elf[0] - 1, elf[1] - 1), (elf[0] + 1, elf[1] + 1), (elf[0] + 1, elf[1] - 1)]
    return not any(position in elves for position in all_positions)
    
def get_positions(elf, test):
    test_positions = []
    #check that there are 8 valid positions around the elf
    if  no_elves(elf):
        return test_positions
    for direction in test.get('tests'):
        match direction:
            case 'N':
                test_positions.append((elf[0] - 1, elf[1]))
            case 'S':
                test_positions.append((elf[0] + 1, elf[1]))
            case 'W':
                test_positions.append((elf[0], elf[1] - 1))
            case 'E':
                test_positions.append((elf[0], elf[1] + 1))
            case 'NE':
                test_positions.append((elf[0] - 1, elf[1] + 1))
            case 'NW':
                test_positions.append((elf[0] - 1, elf[1] - 1))
            case 'SE':
                test_positions.append((elf[0] + 1, elf[1] + 1))
            case 'SW':
                test_positions.append((elf[0] + 1, elf[1] - 1))
    return test_positions
   

def elf_indexes_to_move(positions):
    indexes = []
    hold_positions = []
    dup_positions = []
    for index, position in enumerate(positions):
        if position not in hold_positions:
            indexes.append(index)
            hold_positions.append(position)
        else:
            dup_positions.append(position)
    #now we want to remove the first instance of all dup positions since we keep the first one
    #print(hold_positions, dup_positions)
    dup_indexes = [x for x, position in enumerate(positions) if position in dup_positions]
    return [x for x in indexes if x not in dup_indexes]

#printmap(elves)
#def moves(tests, elves):
attempts = 10
suggestions = []
for attempt in range(attempts):
    stopped = False
    count = 0
#while not stopped:: part b didn't work
    #everyone does their test and proposes
    #print(f'top test {tests[0].get("step")}')
    for index, elf in enumerate(elves):
        for test in tests:
            positions_to_test = get_positions(elf, test)
            if len(positions_to_test) < 3:
                positions_to_test = [(-1, -1)]
            if all(position not in elves for position in positions_to_test):
                suggestions.append(positions_to_test[0])
                break
        #if there's no where for the elf to go, insert the -1 as well
        if len(suggestions) < index + 1:
            #print(f"didn''t find a position for elf {elf} at {index}")
            suggestions.append((-1, -1))
    #all elves have attempted to propose positions, let's figure out who's unique
    #print(suggestions)
    moving_elves = elf_indexes_to_move(suggestions)
    if len(moving_elves) > 0:
        stopped = False
        count += 1
    else:
        stopped = True
        break
    for elf_index in moving_elves:
        if suggestions[elf_index] == (-1, -1):
            continue
        #print(f'moving elf {elves[elf_index]} at {elf_index} to {suggestions[elf_index]}')
        elves[elf_index] = suggestions[elf_index]
    #printmap(elves)
    #reset suggestions
    suggestions = []
    #rearrange the tests
    top = tests.pop(0)
    tests.append(top)



#get largest rectangle
#get top most elf
top = min([x[0] for x in elves])
bottom = max([x[0] for x in elves])
left = min([y[1] for y in elves])
right = max([y[1] for y in elves])
area = ((bottom - top) + 1) * ((right - left) + 1)
empty = area - len(elves)
#printmap(elves)
print(f'total elves: {len(elves)}, area: {top}->{bottom} and {left}->{right};  empty ground tiles {empty}')
print(f'it took {count+1} tries')




