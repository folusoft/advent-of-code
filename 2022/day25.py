import math
lines = open('./day25.txt').readlines()
total = 0

def translate_to_dec(snafu_number):
    match snafu_number:
        case '-':
            return -1
        case '=':
            return -2
        case _:
            return eval(snafu_number)

def translate_to_snafu(decimal):
    match decimal:
        case  0 | 1| 2:
            return str(decimal)
        case -1:
            return '-'
        case -2:
            return '='

def determine_power(number):
    if number == 0:
        return 0
    power = round(math.log(abs(number)) / math.log(5))
    raise5 = 5 ** power
    if int(raise5 / number) >= 2:
        power += -1
    return power

def determine_first(number, power):
    if number in [0, 1, 2] or power == 0:
        return str(number)
    #if the power of the number is less than the passed in power
    if determine_power(number) < power:
        return '0'
    target = 5 ** power
    diff = abs(target - number)
    next_power = determine_power(diff)
    #print(f'get_first## number: {number}, power: {power}, target: {target}, diff: {diff}, next_power: {next_power}')
    if next_power < power:
        return '1'
    return '2'
def convert(number, power):
    #print(f'number: {number}, power: {power}')
    match number:
        case 0 | 1 | 2:
            if power == 0:
                return str(number)
            if power < 0:
                return ''
            else:
                return f'0{convert(number, power - 1)}'
        case -1:
            if power == 0:
                return '-'
            else:
                return f'0{convert(number, power - 1)}'
        case -2:
            if power == 0:
                return '='
            else:
                return f'0{convert(number, power - 1)}'
        case _:
            first = determine_first(abs(number), power)
            first = int(math.copysign(translate_to_dec(first), number))
            remainder = number - (first * (5 ** (power)))
            #print(f'number: {number}, power: {power}, first: ({first}): {translate_to_snafu(first)}, remainder: {remainder}')
            return f'{translate_to_snafu(first)}{convert(remainder, power - 1)}'

for line in lines:
    line = list(line.strip())
    positions = len(line)
    line.reverse()
    for position, number in enumerate(line):
        #print(f'position: {position}; number: {number}')
        number = translate_to_dec(number)
        decimal = (5 ** position)*number
        #print(f'adding {number} ({decimal}) to sum')
        total += decimal

#print(total)
power = determine_power(total)
first = determine_first(total, power)
remainder = total - (translate_to_dec(first) * (5 ** (power)))
print(f'Solution {total}: {first}{convert(remainder, power - 1)}')