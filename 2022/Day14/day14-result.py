# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:19:31 2023

@author: Esa
"""

import os
cwd = os.getcwd()
Day = 14
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
#### Part 1 
max_x_coord = 0
min_x_coord = 9999
max_y_coord = 0
min_y_coord = 0
last = []
current = []
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split(' -> ')
        for k in x:
            y = k.split(',')
            current = [int(y[0]), int(y[1])]
            if current[0] > max_x_coord:
                max_x_coord = current[0]
            elif current[1] > max_y_coord:
                max_y_coord = current[1]
            elif current[0] < min_x_coord:
                min_x_coord = current[0]
        last = []
        current = []
grid_dimensions = [max_x_coord, min_x_coord, max_y_coord, min_y_coord]
grid_size = [0,grid_dimensions[0]-grid_dimensions[1],0,grid_dimensions[2]]

row = []
grid = []
for i in range(grid_size[3]+1):
    row = []
    for j in range(grid_size[1]+1):
        row.append(".")
    grid.append(row)
    
sand_start = [0, 500-min_x_coord]
grid[sand_start[0]][sand_start[1]] = "+"

with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split(' -> ')
        for k in x:
            y = k.split(',')
            current = [int(y[0]), int(y[1])]
            if last == []:
                last = current
                grid[current[1]][current[0]-min_x_coord] = "#"
            else:
                if last[0] != current[0]:
                    for z in range(min(last[0]-min_x_coord, current[0]-min_x_coord), max(last[0]-min_x_coord, current[0]-min_x_coord)+1):
                        grid[last[1]][z] = "#"
                elif last[1] != current[1]:
                    for z in range(min(last[1], current[1]), max(last[1], current[1])+1):
                        grid[z][last[0]-min_x_coord] = "#"
                last = current
        last = []
        current = []

cur_loc = sand_start

def isInGrid(grid, pos):
    isIn = True
    if pos[0] > len(grid)-1 or pos[1] > len(grid[0])-1:
        isIn = False
    return isIn

def canMoveDown(grid, pos):
    if isInGrid(grid, [pos[0]+1, pos[1]]) and grid[pos[0]+1][pos[1]] == ".":
        return [pos[0]+1, pos[1]]
    else:
        return False

def canMoveLeft(grid, pos):
    if isInGrid(grid, [pos[0]+1, pos[1]-1]) and isInGrid(grid, [pos[0], pos[1]-1]) and grid[cur_loc[0]+1][cur_loc[1]-1] == ".":
        return [pos[0]+1, pos[1]-1]

    else:
        return False
    
def canMoveRight(grid, pos):
    if isInGrid(grid, [pos[0]+1, pos[1]+1]) and isInGrid(grid, [pos[0], pos[1]+1]) and grid[cur_loc[0]+1][cur_loc[1]+1] == ".":
        return [pos[0]+1, pos[1]+1]
    else:
            return False

def movedOut(grid, pos):
    if isInGrid(grid, [pos[0]+1, pos[1]]):
        return False
    else:
        return True
    
num_Of_Sand_Grains = 0

while isInGrid(grid, cur_loc):
    #print(cur_loc)
    if movedOut(grid, cur_loc):
        cur_loc = [9999, 9999]
    elif canMoveDown(grid, cur_loc):
        cur_loc = canMoveDown(grid, cur_loc)
    elif canMoveLeft(grid, cur_loc):
        cur_loc = canMoveLeft(grid, cur_loc)
    elif canMoveRight(grid, cur_loc):
        cur_loc = canMoveRight(grid, cur_loc)
    else:
        grid[cur_loc[0]][cur_loc[1]] = "O"
        num_Of_Sand_Grains += 1
        cur_loc = sand_start
        

print("Part 1 answer: " + str(num_Of_Sand_Grains))

### Part 2

max_x_coord = 0
min_x_coord = 9999
max_y_coord = 0
min_y_coord = 0
last = []
current = []
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split(' -> ')

        for k in x:
            y = k.split(',')
            current = [int(y[0]), int(y[1])]
            if current[0] > max_x_coord:
                max_x_coord = current[0]
            elif current[1] > max_y_coord:
                max_y_coord = current[1]
            elif current[0] < min_x_coord:
                min_x_coord = current[0]
        last = []
        current = []
grid_dimensions = [max_x_coord, min_x_coord, max_y_coord, min_y_coord]
grid_size = [0,grid_dimensions[0]-grid_dimensions[1],0,grid_dimensions[2]]

row = []
grid = []
for i in range(grid_size[3]+3):
    row = []
    for j in range(grid_size[1]+1):
        if i > grid_size[3]+1:
            row.append("#")
        else:
            row.append(".")
    grid.append(row)

def extendGrid(grid):
    for i in range(len(grid)):
        if i == len(grid)-1:
            grid[i][:0] = ['#']
            grid[i].append('#')
        else:
            grid[i][:0] = ['.']
            grid[i].append('.')
            



sand_start = [0, 500-min_x_coord]
grid[sand_start[0]][sand_start[1]] = "+"

with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split(' -> ')
        for k in x:
            y = k.split(',')
            current = [int(y[0]), int(y[1])]

            if last == []:
                last = current
                grid[current[1]][current[0]-min_x_coord] = "#"
            else:
                if last[0] != current[0]:
                    for z in range(min(last[0]-min_x_coord, current[0]-min_x_coord), max(last[0]-min_x_coord, current[0]-min_x_coord)+1):
                        grid[last[1]][z] = "#"
                elif last[1] != current[1]:
                    for z in range(min(last[1], current[1]), max(last[1], current[1])+1):
                        grid[z][last[0]-min_x_coord] = "#"
                last = current
        last = []
        current = []
extendGrid(grid)
sand_start = [sand_start[0], sand_start[1]+1]

cur_loc = sand_start



def isInGrid(grid, pos):
    isIn = True
    if pos[0] > len(grid)-1 or pos[1] > len(grid[0])-1 or pos[1] < 0:
        isIn = False
    return isIn

def canMoveDown(grid, pos):
    if isInGrid(grid, [pos[0]+1, pos[1]]) and grid[pos[0]+1][pos[1]] == ".":
        return [pos[0]+1, pos[1]]
    else:
        return False

def canMoveLeft(grid, pos):
    if isInGrid(grid, [pos[0], pos[1]-1]) and grid[pos[0]+1][pos[1]-1] == ".":
        return [pos[0]+1, pos[1]-1]

    else:
        return False
    
def canMoveRight(grid, pos):
    if isInGrid(grid, [pos[0], pos[1]+1]) and grid[pos[0]+1][pos[1]+1] == ".":
        return [pos[0]+1, pos[1]+1]
    else:
            return False

def movedOut(grid, pos):
    if isInGrid(grid, [pos[0], pos[1]-1]) and isInGrid(grid, [pos[0], pos[1]+1]):
        return False
    else:
        return True

num_Of_Sand_Grains = 0

while grid[sand_start[0]][sand_start[1]] != "O": 
    if canMoveDown(grid, cur_loc):
        cur_loc = canMoveDown(grid, cur_loc)
    elif canMoveLeft(grid, cur_loc):
        cur_loc = canMoveLeft(grid, cur_loc)
    elif canMoveRight(grid, cur_loc):
        cur_loc = canMoveRight(grid, cur_loc)
    elif movedOut(grid, cur_loc):
            extendGrid(grid)
            sand_start = [sand_start[0], sand_start[1]+1]
            cur_loc = [cur_loc[0], cur_loc[1]+1]
    else:
        grid[cur_loc[0]][cur_loc[1]] = "O"
        num_Of_Sand_Grains += 1
        cur_loc = sand_start

print("Part 2 answer: " + str(num_Of_Sand_Grains))