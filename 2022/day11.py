import numpy as np
lines = open('day11.txt', 'r').readlines()

##TODO need to figure out part 2

class Monkey():
    def __init__(self, items, operation, test, t_monkey, f_monkey):
        self.items = items
        self.magnitude = operation.split('=')[1].split(' ')[3]
        self.operation = operation.split('=')[1].split(' ')[2]
        self.test_magnitude = eval(test.split('by')[1])
        self.t_monkey = eval(t_monkey.split(' ')[-1])
        self.f_monkey = eval(f_monkey.split(' ')[-1])
        self.total = 0

    def serialize(self):
        return (f'{self.items}, {self.operation}, {self.magnitude}, {self.test_magnitude}, {self.t_monkey}, {self.f_monkey}')

instructions = []
monkeys = {}
counter = 0
for line in lines:
    line = line.strip()
    if len(line.strip()) == 0:
        continue
    if 'false' in line:
        #process the monkey_lines
        instructions.append(line)
        #monkey = Monkey(instructions[1].split(':')[1], instructions[2], instructions[3], instructions[4], instructions[5])
        monkeys[counter] = {'items' : instructions[1].split(':')[1], 'magnitude': instructions[2].split('=')[1].split(' ')[3], \
                            'operation' : instructions[2].split('=')[1].split(' ')[2],  'test_magnitude' : eval(instructions[3].split('by')[1]), \
                                't_monkey' : eval(instructions[4].split(' ')[-1]), 'f_monkey' : eval(instructions[5].split(' ')[-1]), \
                                    'total' : 0}
        counter += 1
        #monkeys.append(monkey)
        instructions = []
    else:
        instructions.append(line)

worry_divider = 1
for round in range(10000):
    print(f'starting round number {round+1}')
    for index in monkeys.keys():
        # print(f'{index}, {monkey.serialize()}')
        #loop through the monkey's items
        monkey = monkeys.get(index)
        items = monkey['items'].split(',')
        for item in items:
            if item == '':
                continue
            #calculate worry
            #print(f'round {round} Monkey {index} [{items}] {item}')
            worry = eval(item)
            #print(f'Monkey {index} with {monkey.items} inspects an item with worry level of {worry}')
            if monkey['magnitude'].isnumeric():
                magnitude = eval(monkey['magnitude'])
            else:
                magnitude = eval(item)
            match(monkey['operation']):
                case '*':
                    worry  = worry * magnitude
                    #print(f'Monkey {index} worry level is multiplied by {magnitude} to {worry}')
                case '+':
                    worry += magnitude
                    #print(f'Monkey {index} worry level is increased by {magnitude} to {worry}')
            #divide worry
            worry = worry // worry_divider
            #test
            if worry % monkey['test_magnitude'] == 0:
                monkeys.get(monkey['t_monkey'])['items'] = monkeys.get(monkey['t_monkey'])['items'] + f", {worry}"
                #print(f'Monkey {index} current worry level is divisible by {monkey.test_magnitude} so passing {worry} to {monkey.t_monkey}')
            else:
                monkeys.get(monkey['f_monkey'])['items'] = monkeys.get(monkey['f_monkey'])['items'] + f", {worry}"
                #print(f'Monkey {index} current worry level is not divisible by {monkey.test_magnitude} so passing {worry} to {monkey.f_monkey}')
            monkey['items'] = "".join(monkey['items'].split(f'{item}, ')[1:])
            #print(f'Monkey {index} now has {monkey.items} left')
            monkey['total'] =  monkey['total'] + 1
runs = []
for index in monkeys.keys():
    runs.append(monkeys.get(index)['total'])
    print(f'{index}, {monkeys.get(index)["total"]}')

top = max(runs)
runs.remove(top)
print(f'{top}, {max(runs)}')
print(f'{top * max(runs)}')



        