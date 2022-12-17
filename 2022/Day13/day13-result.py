# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:17:14 2022

@author: Esa
"""
import os
cwd = os.getcwd()
Day = 13
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

import json
from functools import cmp_to_key

selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
left = None
right = None


def walkLists(list1, list2):
    list1 = list1 if isinstance(list1, list) else [list1]
    list2 = list2 if isinstance(list2, list) else [list2]
    for x, y in zip(list1, list2):
        if isinstance(x, list) or isinstance(y, list):
            result = walkLists(x, y)
        else:
            result = y - x
        if result != 0:
            return result
    return len(list2) - len(list1)

scr = 0
numOfPairs = 0
index1 = 1
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        if left == None and right == None:
            left = x
        elif left != None and right == None:
            right = x
            a = json.loads(left)
            b = json.loads(right)
            if walkLists(a, b) > 0:
                numOfPairs += index1
        elif x == "":
            left = None
            right = None
            #print("pass")
            index1 += 1
print(numOfPairs)

### Part 2
divPacks = [[[2]], [[6]]]
temp = []
temp2 = []
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        if x != "":
            a = json.loads(x)
            temp.append(a)
        elif x == "":
            temp2.append(temp)
            temp = []
    if len(temp) == 2:
        temp2.append(temp)
        temp = []

sortedSet = sorted([i for j in temp2 for i in j] + divPacks, key=cmp_to_key(walkLists), reverse=True)
index2 = 1
temp3 = []
for i in sortedSet:
    if i == [[2]] or i == [[6]]:
        temp3.append(index2)
    index2 += 1
result = temp3[0] * temp3[1]
print(result)