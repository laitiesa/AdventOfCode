# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:05:21 2022

@author: Esa
"""

import copy
import os
cwd = os.getcwd()
Day = 10
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
cycle = 0
X = 1
Xstrengths = []
instructions = {'noop': 1, 'addx': 2}
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split()
        instruction = instructions[x[0]]
        for j in range(instruction):
            cycle += 1
            if cycle >= 20 and (cycle-20) % 40 == 0:
                Xstrengths.append([cycle, cycle*X])
                if j == instruction-1 and x[0] == 'addx':
                    X += int(x[1])
                #print(cycle, X)
            elif j == instruction-1 and x[0] == 'addx':
                X += int(x[1])
        
            
            
# print(Xstrengths)
answer = 0
for k, v in Xstrengths:
    if k < 221:
        answer  += v
print(answer)

### PART 2
# screen = []
# for i in range(6):
#     screen.append([])
#     for j in range(40):
#         screen[i].append('.')
# # for k in screen:
# #     print(k)
cycle = 0
X = 1
sprite = [X-1, X, X+1]
dummyScreen = []
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip().split()
        instruction = instructions[x[0]]
        if cycle < 241:
            for j in range(instruction):
                
                cycle += 1
                #print((cycle % 40)-1)
                #print(sprite)
                #print((cycle % 40) in sprite)
                if (cycle % 40)-1 in sprite:
                    dummyScreen.append('#')
                else:
                    dummyScreen.append(' ')
                if j == instruction-1 and x[0] == 'addx':
                        X += int(x[1])
                        sprite = [X-1, X, X+1]
        else:
            break
#print(dummyScreen)
screen = [[dummyScreen[0:40]],[dummyScreen[40:80]],[dummyScreen[80:120]],[dummyScreen[120:160]],[dummyScreen[160:200]],[dummyScreen[200:240]]]
for k in range(len(screen)):
    z = (' '.join(str(e) for e in screen[k]))
    print(z)