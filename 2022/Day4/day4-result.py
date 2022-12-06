# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:20:23 2022

@author: Esa
"""

import os
cwd = os.getcwd()
Day = 4
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
# Part 1
pairs = 0
with open(selectedInput) as f:
    for i in f:
        z = i.rstrip().split(",")
        x = z[0].split("-")
        y = z[1].split("-")
        x2 = [int(j) for j in range(int(x[0]),int(x[1])+1)]
        y2 = [int(k) for k in range(int(y[0]),int(y[1])+1)]
        if len(x2) > len(y2):
            result = all(elem in x2 for elem in y2)
        else:
            result = all(elem in y2 for elem in x2)
        if result:
            pairs += 1
print(pairs)


# Part 2
pairs = 0
with open(selectedInput) as f:
    for i in f:
        z = i.rstrip().split(",")
        x = z[0].split("-")
        y = z[1].split("-")
        x2 = [int(j) for j in range(int(x[0]),int(x[1])+1)]
        y2 = [int(k) for k in range(int(y[0]),int(y[1])+1)]
        if len(x2) > len(y2):
            result = any(elem in x2 for elem in y2)
        else:
            result = any(elem in y2 for elem in x2)
        if result:
            pairs += 1
print(pairs)