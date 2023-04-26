# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:03:00 2023

@author: Esa
"""
import time
import os
cwd = os.getcwd()
Day = 15
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
### coordinateList in form [x1, y1, x2, y2]    
def calculateManhattanDistance(coordinateList):
    min_x, max_x = min(coordinateList[0], coordinateList[2]), max(coordinateList[0], coordinateList[2])
    min_y, max_y = min(coordinateList[1], coordinateList[3]), max(coordinateList[1], coordinateList[3])
    distance = (max_x - min_x) + (max_y - min_y)
    return distance

def calculateSensorRangeOnRowY(sensorCoords, Y):
    max_Dist = sensorCoords[1]
    y_Dist = max(sensorCoords[0][1], Y) - min(sensorCoords[0][1], Y)
    sensor_x_Dist = sensorCoords[0][0]
    if y_Dist <= max_Dist:
        plus_x_Dist = [(max_Dist - y_Dist + sensor_x_Dist), Y]
        minus_x_Dist = [((max_Dist - y_Dist) * -1) + sensor_x_Dist, Y]
        return [minus_x_Dist, plus_x_Dist]
    else:
        return False

    
#### Part 1 
sensor_Set = []
beacons = []

tic = time.perf_counter()

with open(selectedInput) as f:
    for i in f:
        line = i.rstrip().split()
        sensor_x = int(line[2].rstrip('x=,').lstrip('x=,'))
        sensor_y = int(line[3].rstrip('y=:,').lstrip('y=,'))
        beacon_x = int(line[8].rstrip('x=,').lstrip('x=,'))
        beacon_y = int(line[-1].rstrip('y=:,').lstrip('y=:,'))
        sensor_Set.append([[sensor_x, sensor_y, beacon_x, beacon_y], calculateManhattanDistance([sensor_x, sensor_y, beacon_x, beacon_y])])
        beacon = [beacon_x, beacon_y]
        if beacon not in beacons:
            beacons.append(beacon)

y_Coord = 0
if test:
    y_Coord = 10
else:
    y_Coord = 2000000



Ranges = []
for k in sensor_Set:
    temp = calculateSensorRangeOnRowY(k, y_Coord)

    if temp:
        x_range = [temp[0][0], temp[1][0]]
        Ranges.append(x_range)
temp2 = sorted(Ranges)
cur_min_x = 0
cur_max_x = 0
positions = 0

for k in temp2:
    if k[0] < cur_min_x:
        cur_min_x = k[0]
    elif k[1] > cur_max_x:
        if cur_max_x == 0:
            positions += abs(cur_min_x - k[1])
        else:
            positions += abs(cur_max_x - k[1])
        cur_max_x = k[1]

toc = time.perf_counter()
print(f"Part 1 solution {positions}")
print(f"Part 1 solved in {toc - tic:0.4f} seconds")

### Part 2

if test:
    y_Coord = 21
else:
    y_Coord = 4000001



tic = time.perf_counter()

for i in range(0, y_Coord):
    Ranges = []
    for k in sensor_Set:
        temp = calculateSensorRangeOnRowY(k, i)

        if temp:
            x_range = [temp[0][0], min(y_Coord, temp[1][0])]
            if x_range[0] <= y_Coord:
                Ranges.append(x_range)
    temp2 = sorted(Ranges)

    cur_min_x = 0
    cur_max_x = 0
    range_sets = []
    for k in temp2:
        if k[0] > cur_max_x+1 and cur_max_x != 0:
            range_sets.append([cur_min_x, cur_max_x])
            cur_min_x = k[0]
            cur_max_x = k[1]
        elif k[1] > cur_max_x:
            cur_max_x = k[1]

    range_sets.append([cur_min_x, cur_max_x])

    if len(range_sets) > 1:
        
        x_coord = (range_sets[1][0]+1-(range_sets[1][0] - range_sets[0][1]))
        y_coord = i
        frequency = x_coord * 4000000 + y_coord
        print(f"Part 2 solution: {frequency}")
        break
toc = time.perf_counter()
print(f"Part 2 solved in {toc - tic:0.4f} seconds")
print(f"Stopped on row {i}")