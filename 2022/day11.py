import time
import pandas as pd
from math import prod
lines = open('day11.txt', 'r').readlines()
monkeys = []
analysis = []
def operation(v1, op, v2):
    match op:
        case '+':
            return v1 + v2
        case '*':
            return v1 * v2

def parse_monkey(line):
    return {
        "id" : eval(lines[line].split(' ')[1].split(':')[0]),
        "items" : [eval(x) for x in lines[line + 1].split(': ')[1].split(', ')],
        "operation" : lines[line + 2].split("= ")[1].strip().split(' '),
        "testnum" : eval(lines[line + 3].split('by ')[1]),
        "test" : lambda x: x % eval(lines[line + 3].split('by ')[1]) == 0,
        "true" :  eval(lines[line + 4].strip().split('monkey ')[1]),
        "false" : eval(lines[line + 5].strip().split('monkey ')[1]),
        "total" : 0
    }, line + 7

line_counter = 0
while line_counter < len(lines):
   monkey, line_counter = parse_monkey(line_counter)
   monkeys.append(monkey)
   
   
worry_divider =  prod(m["testnum"] for m in monkeys) #this is for part 2
# The more worried you are, the more complex the problem and the longer it runs. Ensuring that your worry always reduces prior to the test helps
# In part 1, it's divided by 3. In part 2, we get the remainder of a sum product of all the test numbers (which are prime like 3. their product is also a prime). 
RUNS = 10000
start = time.perf_counter()
for round in range(RUNS):
    # print(f'starting round number {round+1}')
    for monkey in monkeys:
        for item in monkey['items']:
            parameters = monkey['operation']
            v1, op, v2 = item, parameters[1], item if parameters[2] == "old" else eval(parameters[2])
            worry = operation(v1, op, v2)
            if worry_divider == 3:
                worry //= worry_divider
            else:
                worry %= worry_divider
            test = monkey['test'](worry)
            if test:
                monkeys[monkey['true']].get('items').append(worry)
            else:
                monkeys[monkey['false']].get('items').append(worry)
            monkey['total'] =  monkey['total'] + 1
        monkey['items'] = []
    if (round+1) % 1000 == 0:
        result = {'runs' : round+1}
        for monkey in monkeys:
            result[monkey['id']] = monkey['total']
        analysis.append(result)

end = time.perf_counter()
print(f'{RUNS} completed in {end - start:0.4f} seconds')
runs = []
for monkey in monkeys:
    runs.append(monkey['total'])
    print(f'Monkey: {monkey["id"]}, {monkey["total"]}')
top = max(runs)
runs.remove(top)
# print(f'{top}, {max(runs)}')
print(f'{top * max(runs)}')
print(pd.DataFrame(analysis))
pd.DataFrame(analysis).to_csv('./output.csv')
