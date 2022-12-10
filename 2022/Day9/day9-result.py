# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:07:48 2022

@author: Esa
"""
import copy
import os
cwd = os.getcwd()
Day = 9
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
test_input2 =  cwd + "/test-input-" + str(Day) + "-2" + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

selectedInput = None
test = False
test2 = False
if test and test2:
    selectedInput = test_input2
elif test:
    selectedInput = test_input
else:
    selectedInput = real_input

from collections import defaultdict
import numpy as np
### Part 1

# start = [0, 0]
# headVisits = 0
# visited = [[0, 0]]
# tailVisited = [[0, 0]]
# tailpos = [0,0]
# with open(selectedInput) as f:
#     for i in f:
#         x = i.rstrip().split()
#         #print(x)
#         if x[0] == 'R':
#             for y in range(int(x[1])):
#                 start[1] += 1
#                 pos = [start[0],start[1]]
#                 visited.append(pos)
#                 if abs(pos[0] - tailpos[0]) > 1 or abs(pos[1] - tailpos[1]) > 1:
#                         tailpos = visited[-2]
#                         if tailpos not in tailVisited:
#                             tailVisited.append(tailpos)
#         elif x[0] == 'L':
#             for y in range(int(x[1])):
#                 start[1] -= 1
#                 pos = [start[0],start[1]]
#                 visited.append(pos)
#                 if abs(pos[0] - tailpos[0]) > 1 or abs(pos[1] - tailpos[1]) > 1:
#                         tailpos = visited[-2]
#                         if tailpos not in tailVisited:
#                             tailVisited.append(tailpos)
#         elif x[0] == 'U':
#             for y in range(int(x[1])):
#                 start[0] += 1
#                 pos = [start[0],start[1]]
#                 visited.append(pos)
#                 if abs(pos[0] - tailpos[0]) > 1 or abs(pos[1] - tailpos[1]) > 1:
#                         tailpos = visited[-2]
#                         if tailpos not in tailVisited:
#                             tailVisited.append(tailpos)
#         elif x[0] == 'D':
#             for y in range(int(x[1])):
#                 start[0] -= 1
#                 pos = [start[0],start[1]]
#                 visited.append(pos)
#                 if abs(pos[0] - tailpos[0]) > 1 or abs(pos[1] - tailpos[1]) > 1:
#                         tailpos = visited[-2]
#                         if tailpos not in tailVisited:
#                             tailVisited.append(tailpos)
# print("Part 1: " + str(len(tailVisited)))

directions = {'R': [0,1], 'L': [0,-1], 'U': [1,0], 'D': [-1,0],}
direction = []
rope = { 0: {'current': [0, 0], 'last': [0, 0], 'direction': None}, 1: {'current': [0, 0], 'last': [0, 0], 'direction': None}}
headVisited = [[0, 0]]
tailVisited = [[0, 0]]
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split()
        direction = directions[x[0]]
        for y in range(int(x[1])):
            rope[0]['last'] = rope[0]['current']
            rope[0]['direction'] = direction
            rope[0]['current'] = [rope[0]['current'][0] + direction[0], rope[0]['current'][1] + direction[1]]
            headVisited.append(rope[0]['current'])
            for k in range(1, len(rope)):
                yoffset = rope[k-1]['current'][0] - rope[k]['current'][0]
                xoffset = rope[k-1]['current'][1] - rope[k]['current'][1]
                if yoffset**2 + xoffset**2 > 2:
                   if k == len(rope)-1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['current'] = [rope[k]['last'][0] + np.sign(yoffset), rope[k]['last'][1] + np.sign(xoffset)]
                       tailPos = rope[k]['current']
                       if tailPos not in tailVisited:
                           tailVisited.append(tailPos)
                   elif k != 1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['current'] = [rope[k]['last'][0] + np.sign(yoffset), rope[k]['last'][1] + np.sign(xoffset)]
                   elif k == 1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['direction'] = direction
                       rope[k]['current'] = rope[k-1]['last']
print("Part 1: " + str(len(tailVisited)))


### Part 2

directions = {'R': [0,1], 'L': [0,-1], 'U': [1,0], 'D': [-1,0],}
direction = []
rope = { 0: {'current': [0, 0], 'last': [0, 0]}, 
        1: {'current': [0, 0], 'last': [0, 0]},
        2: {'current': [0, 0], 'last': [0, 0]},
        3: {'current': [0, 0], 'last': [0, 0]},
        4: {'current': [0, 0], 'last': [0, 0]},
        5: {'current': [0, 0], 'last': [0, 0]},
        6: {'current': [0, 0], 'last': [0, 0]},
        7: {'current': [0, 0], 'last': [0, 0]},
        8: {'current': [0, 0], 'last': [0, 0]},
        9: {'current': [0, 0], 'last': [0, 0]},
        }
headVisited = [[0, 0]]
tailVisited = [[0, 0]]
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split()
        direction = directions[x[0]]
        for y in range(int(x[1])):
            rope[0]['last'] = rope[0]['current']
            rope[0]['current'] = [rope[0]['current'][0] + direction[0], rope[0]['current'][1] + direction[1]]
            headVisited.append(rope[0]['current'])
            for k in range(1, len(rope)):
                yoffset = rope[k-1]['current'][0] - rope[k]['current'][0]
                xoffset = rope[k-1]['current'][1] - rope[k]['current'][1]
                if yoffset**2 + xoffset**2 > 2:
                   if k == len(rope)-1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['current'] = [rope[k]['last'][0] + np.sign(yoffset), rope[k]['last'][1] + np.sign(xoffset)]
                       tailPos = rope[k]['current']
                       if tailPos not in tailVisited:
                           tailVisited.append(tailPos)
                   elif k != 1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['current'] = [rope[k]['last'][0] + np.sign(yoffset), rope[k]['last'][1] + np.sign(xoffset)]
                   elif k == 1:
                       rope[k]['last'] = rope[k]['current']
                       rope[k]['direction'] = direction
                       rope[k]['current'] = rope[k-1]['last']
print("Part 2: " + str(len(tailVisited)))
