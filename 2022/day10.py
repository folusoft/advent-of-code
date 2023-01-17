lines = open('day10.txt', 'r').readlines()
X = 1
counter = []
counter.append('.')

def add_counter(line, lines, index):
    counter.append(X)


def value_cycle(cycle):
    #we want the value during a particular cycle. If the prior cycle has a different value, it means during
    #this one, we have the same one as values only change at the end of cycle
    if cycle <= 1:
        return 0
    if counter[cycle-1] != counter[cycle]:
        return counter[cycle-1]
    else:
        return counter[cycle]

def pixel_positions(value):
    match value:
        case 0 :
            return [value]
        case 1:
            return [0, 1]
        case _:
            return [value-1, value, value+1]


for index, line in enumerate(lines):
    line = line.strip()
    command = line.split(' ')[0]
    match command:
        case 'noop':
            #nothing happens, insert current value of X after 1 cycle
            add_counter(line, lines, index)
        case 'addx':
            #ok do a counter for two during which we append X then after we append 
            for count in range(1):
                add_counter(line, lines, index)
            unit = eval(line.split(' ')[1])
            X += unit
            add_counter(line, lines, index)

# for index, value in enumerate(counter):
#     print(f'cycle: {index}, during value: {value_cycle(index)}, end value: {value}')

signal_strength = 0
for index in [20, 60, 100, 140, 180, 220]:
    signal_strength += index * value_cycle(index)
    #print(f'cycle: {index}, value: {value_cycle(index)}, product: {index*value_cycle(index)}')
print(signal_strength)

for cycle in range(1, 240, 40):
    screen = ['.'] * 40
    #print(str(screen))
    for index in range(cycle, (cycle + 40), 1):
        value = value_cycle(index)
        pixels = pixel_positions(value)
        #printing position = cycle % 40
        position = (index-1) % 40
        for pixel in pixels:
            if pixel == position:
                screen[position] = '#'
    print(screen)

    


