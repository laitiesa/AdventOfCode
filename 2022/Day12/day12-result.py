# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:05:27 2022

@author: Esa
"""


import os
cwd = os.getcwd()
Day = 12
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

from collections import  deque


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
index1 = 0
index2 = 0
Start = []
End = []
grid = []
startList = []
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        temp = []
        index2 = 0
        for j in x:
            if j.islower():
                temp.append(ord(j)-96)
                if ord(j)-96 == 1:
                    startList.append([index1, index2])
            elif j == 'S':
                Start = [index1, index2]
                temp.append(0)
            elif j == 'E':
                End = [index1, index2]
                temp.append(27)
            index2 += 1
        grid.append(temp)
        index1 += 1


def isValidValue(current, new, grid):
    new = grid[new[0]][new[1]]
    return new <= current or new == current + 1

def isWithingGrid(pos, grid):
    row = pos[0]
    col = pos[1]
    max_row = len(grid)
    max_col = len(grid[0])
    return (row >= 0) and (row < max_row) and (col >= 0) and (col < max_col)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
class Node:
    def __init__(self, point: Point, distance: int):
        self.point = point
        self.distance = distance


q = deque()
Start = Node(Point(Start[0], Start[1]), 0)
q.append(Start)
add = []
seen = [[Start]]
steps = []
done = False
allSteps = [[-1, 0], [0, -1], [0, 1], [1, 0]]
distance = 0

#### Part 1
while q:
    add = q.popleft()
    curpoint = add.point
    row = curpoint.x
    col = curpoint.y
    value = grid[row][col]

    if add.distance > distance:
        distance = add.distance
    if value == 27:
        print(add.distance)
        break
    
    for j in allSteps:
        row2 = row + j[0]
        col2 = col + j[1]
        if isWithingGrid([row2, col2], grid) and isValidValue(value, [row2, col2], grid) and [row2, col2] not in seen:
            seen.append([row2, col2])
            adjacent = Node(Point(row2, col2), add.distance + 1)
            q.append(adjacent)
        else:
            continue

### Part 2
minimum = 9999
for k in startList:
    q = deque()
    #print(Start, End)
    Start = Node(Point(k[0], k[1]), 0)
    q.append(Start)
    add = []
    seen = [[k[0], k[1]]]
    steps = []
    done = False
    allSteps = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    distance = 0

    while q:
        add = q.popleft()
        curpoint = add.point
        #value = grid[curpoint[0]][curpoint[1]]
        #print("curpoint")
        #print(curpoint.x, curpoint.y)
        row = curpoint.x
        col = curpoint.y
        value = grid[row][col]
        
        #print(seen)
        if add.distance > distance:
            #print(add.distance)
            distance = add.distance
        if value == 27:
            if add.distance < minimum:
                minimum = add.distance
            break
        
        for j in allSteps:
           # print(j)
            row2 = row + j[0]
            col2 = col + j[1]
            #print("muu")
            # print("Node")
            # print([row2, col2])
            # print("grid")
            # print(isWithingGrid([row2, col2], grid))
            # if isWithingGrid([row2, col2], grid):
            #     print("valid")
            #     print(isValidValue(value, [row2, col2], grid))
            #     print("seen")
            #     print([row2, col2] not in seen)
            if isWithingGrid([row2, col2], grid) and isValidValue(value, [row2, col2], grid) and [row2, col2] not in seen:
                seen.append([row2, col2])
                adjacent = Node(Point(row2, col2), add.distance + 1)
                q.append(adjacent)
            else:
                continue
            #print(put[1:])
            #print(len(put[:1]))
            #print(checkPath(grid, put[1:], Start))
    #print(len(add)-1)
print(minimum)