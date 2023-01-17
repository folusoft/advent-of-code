lines = open('day21.txt', 'r').readlines()

monkeys = dict()

for line in lines:
    line = line.strip()
    #root: pppw + sjmn
    #dbpl: 5
    monkey, operations = line.split(': ')
    operations = operations.split(' ')
    if len(operations) == 1:
        monkeys[monkey] = {'value' : operations[0]}
    else:
        operation = operations[1]
        left_monkey = operations[0]
        right_monkey = operations[2]
        monkeys[monkey] = {'left' : left_monkey, 'right' : right_monkey, 'operation': operation, 'value' : 'NA'}

def find_value(monkey):
    if monkeys.get(monkey).get('value').isnumeric():
        return monkeys.get(monkey).get('value')
    left = find_value(monkeys.get(monkey).get('left'))
    right = find_value(monkeys.get(monkey).get('right'))
    operation = monkeys.get(monkey).get('operation')
    match operation:
        case '+':
            monkeys[monkey] = {'value' : str(eval(left) + eval(right))}
        case '-':
            monkeys[monkey] = {'value' : str(eval(left) - eval(right))}
        case '*':
            monkeys[monkey] = {'value' : str((eval(left)) * eval(right))}
        case '/':
            monkeys[monkey] = {'value' : str((eval(left)) / eval(right))}
    return monkeys.get(monkey).get('value')

def contains_human(monkey):
    match monkeys.get(monkey).get('value').isnumeric():
        case True:
            return False
        case False:
            if monkeys.get(monkey).get('left') == 'humn' or monkeys.get(monkey).get('right')  == 'humn':
                return True
            if not contains_human(monkeys.get(monkey).get('left')):
                return contains_human(monkeys.get(monkey).get('right'))
    return True

def get_non_human(human_side, monkey):
    if len(human_side) == 0:
        human_side = monkey
    print(monkey, human_side)
    if monkeys.get(monkey).get('value').isnumeric() or monkey == 'humn':
        if monkey != 'humn':
            human_side = human_side.replace(monkey, monkeys.get(monkey).get('value'))
        return  
    left =  monkeys.get(monkey).get('left')
    right = monkeys.get(monkey).get('right')
    operation = monkeys.get(monkey).get('operation')
    human_side = human_side.replace(monkey, f'( {left} {operation} {right}')
    return

dup_monkeys = monkeys.copy()
print(find_value('root')) 
monkeys = dup_monkeys.copy()

left = monkeys.get('root').get('left')
right = monkeys.get('root').get('right')

if not contains_human(left):
    left_value = find_value(left)
    right_value = str(1 - eval(left_value))
    counter = 0
    while eval(right_value) != eval(left_value):
        monkeys = dup_monkeys.copy()
        monkeys['humn'] = {'value' : str(counter)}
        right_value = find_value(right)
        #print(f'got {left_value} with counter {monkeys["humn"].get("value")} compared to {right_value}')
        counter += 1
else:
    right_value = find_value(right)
    left_value = str(1 - eval(right_value))
    counter = 3243420789700 
    while eval(left_value) != eval(right_value):
        monkeys = dup_monkeys.copy()
        monkeys['humn'] = {'value' : str(counter)}
        left_value = find_value(left)
        print(f'got {left_value} with counter {monkeys["humn"].get("value")} compared to {right_value}')
        if eval(left_value) < eval(right_value):
            break
        counter += 1

print(left_value, right_value, counter-1)
    


    