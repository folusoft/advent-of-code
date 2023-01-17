from collections import deque
lines = open('day20.txt', 'r').readlines()
##TODO need to figure out part 2

def rotate():
    print("This one stinks!!")
    coordinates = [eval (x) for x in lines]
    for line in lines:
        line = eval(line)
        #print(f'rotating {line}')
        curr_location = coordinates.index(line)
        remainder = (line + curr_location)//len(coordinates)
        new_loc = (curr_location + line + remainder)%len(coordinates)
        hold = coordinates.copy()
        coordinates.pop(curr_location)
        coordinates.insert(new_loc, line)
        #print(f'################\noriginal list: {hold}, moving {line} from {curr_location} to {new_loc} yields {coordinates}. FYI remainder is {remainder}')
    return coordinates

def rotate2():
    coordinates = [(index, eval(x)) for index, x in enumerate(lines)]
    for index, line in enumerate(lines):
        item = (index, eval(line))
        curr_location = coordinates.index(item)
        remainder = (item[1] + curr_location)//len(coordinates)
        new_loc = (curr_location + item[1] + remainder)%len(coordinates)
        coordinates.pop(curr_location)
        coordinates.insert(new_loc, item)

    return [x[1] for x in coordinates]

def rotate3():
    multiplier = 811589153
    coordinates = [(index, eval(x) * multiplier) for index, x in enumerate(lines)]
    for count in range(1):
        for index, line in enumerate(lines):
            item = (index, eval(line) * multiplier)
            curr_location = coordinates.index(item)
            remainder = (item[1] + curr_location)//len(coordinates)
            new_loc = (curr_location + item[1] + remainder)%len(coordinates)
            coordinates.pop(curr_location)
            coordinates.insert(new_loc, item)
            print(f'{[x[1] for x in coordinates]}')
    return [x[1] for x in coordinates]


def counter(coordinates):
    accum = []
    for count in range(3001):
        item = coordinates[count%len(coordinates)]
        match count:
            case 1000:
                print(f'1000th: {item}')
                accum.append(item)
            case 2000:
                print(f'2000th: {item}')
                accum.append(item)
            case 3000:
                print(f'3000th: {item}')
                accum.append(item)

    print(sum(accum))
    #print(coordinates)

def zerofy(coordinates):
    zero_coordinate = coordinates.index(0)
    if zero_coordinate != 0:
        zero_list = coordinates[zero_coordinate:]
        zero_list.extend(coordinates[0:zero_coordinate])
        coordinates = zero_list
    return coordinates

coordinates = rotate3()
print(coordinates)
coordinates = zerofy(coordinates)
counter(coordinates)
#print(coordinates)



