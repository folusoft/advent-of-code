import itertools
from itertools import product
lines = open('day15.txt', 'r').readlines()
##TODO need to figure out part 2

sensors = {}
no_beacons = set()
min_x, max_x = 1000,-1000
min_y, max_y = 1000,-1000

for line in lines:
    line = line.strip()
    x1, x2 = eval(line.split('x=')[1].split(',')[0]), eval(line.split('x=')[2].split(',')[0])
    y1, y2 = eval(line.split('y=')[1].split(':')[0]), eval(line.split('y=')[2].split(':')[0])
    sensors[(x1, y1)] = (x2, y2)
    min_y, min_x = min([min_y, y1, y2]),  min([min_x, x1, x2])
    max_y, max_x = max([max_y, y1, y2]),  max([max_x, x1, x2])

def calculate_manhattan(beacon, sensor):
    x1, x2 = beacon[0], sensor[0]
    y1, y2 = beacon[1], sensor[1]
    return abs(x1-x2) + abs(y1-y2)

#print(sensors)
print(f'max y: {max_y} min y: {min_y}, max x: {max_x}, min x: {min_x}')
def p1():
    y = 2000000
    for index, sensor in enumerate(sensors.keys()):
        beacon = sensors.get(sensor)
        man_dist = calculate_manhattan(beacon, sensor)
        print(f'calculating for sensor: {sensor} at {index+1} out of {len(sensors.keys())} with manhattan distance: {man_dist}')
        for count in range(0, man_dist + 1):
            if (sensor[1] + count) == y or (sensor[1] - count) == y:
                for x in range((sensor[0] + count - man_dist), sensor[0] - count + man_dist + 1):
                    if (x, sensor[1] + count) not in sensors.values():
                        no_beacons.add((x, sensor[1] + count))
                    if (x, sensor[1] - count) not in sensors.values():
                        no_beacons.add((x, sensor[1] - count))  
    no_beacons_at_y = len([x[1] for x in no_beacons if x[1] == y])
    print(f'there are {no_beacons_at_y} positions with no beacons at y={y}')



