from functools import cmp_to_key
lines = open('day13.txt', 'r').read()
pairs = lines.split('\n\n')

packets = []

def compare(left, right):
    # print(f'comparing {left} and {right}')
    if type(left) == type(right) and type(left).__name__ == 'int':
        if left - right < 0:
            return -1
        if left - right > 0:
            return 1
        return 0
    elif type(left) == type(right) and type(left).__name__ == 'list':
        lists = list(zip(left, right))
        for item in lists:
            matched = compare(item[0], item[1])
            if matched:
                return matched
            else:
               continue
        return len(left) - len(right)
    else:
        if type(left).__name__ == 'int':
            #if we're here, it means right is a list
            return compare([left], right)
        else:
            #if we're here it means left is list and right is int
            return compare(left, [right])


same = []
for index, pair in enumerate(pairs):
    #ok now we will process each pair
    left = eval(pair.split('\n')[0])
    right = eval(pair.split('\n')[1])
    packets.append(left)
    packets.append(right)
    matched = compare(left, right)
    if matched < 0:
        same.append(index +1)

# print(len(pairs))
# print(same)
print(sum(same))

packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key=cmp_to_key(compare))
for packet in packets:
    print(packet)

d1 = packets.index([[2]]) + 1
d2 = packets.index([[6]]) + 1
print(f'{d1} * {d2} = {d1 * d2}')