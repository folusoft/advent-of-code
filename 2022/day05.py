import re
file1 = open('day5.txt', 'r')
lines = file1.readlines()

def count_num_stacks(lines):
    index = 0
    for line in lines:
        if 'move' not in line and len(line) > 2 and '[' not in line:
            line = re.sub(r"[\n\t\s]*", "", line)
            num_stacks = int(line[len(line) - 1])
            return index + 1, num_stacks
            
stack_def_index, num_stacks = count_num_stacks(lines)
stacks = [[] for item in range(num_stacks + 1)]
for line in lines:
    #process
    if '[' in line:
        length = len(line)
        divider = int(length/num_stacks)
        stack_index = 1
        pointer = 0
        while pointer < length:
            item = line[pointer:pointer + divider-1]
            if '[' in item:
                stacks[stack_index].append(item)
            pointer = pointer + divider
            stack_index = stack_index + 1
    if'move' in line:
        #execute moves
        commands = line.split(' ')
        count, source_index, target_index = int(commands[1]), int(commands[3]), int(commands[5])
        #part A for counter in range(count):
        #part B
        while count > 0:
            stacks[target_index].insert(0, stacks[source_index].pop(count-1)) # 0 for part A
            count = count - 1 #not needed for part A

stacks.pop(0)
result = "".join(array[0][1:2] for array in stacks)
print(result)


