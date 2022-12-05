# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:48:29 2022

@author: Esa
"""

import os
user = os.path.expanduser('~')
AoCDir = "/OneDrive/Tiedostot/AdventOfCode/2022/Day"
Day = 5
test_input =  user + AoCDir + str(Day) + "/test-input-" + str(Day) + ".txt"
real_input =  user + AoCDir + str(Day) + "/input-" + str(Day) + ".txt"


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
# Part 1

basicDict = {}
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        if x.find("move") == -1 and x.find("[") != -1:
            index = 0
            index2 = 0
            for xx in x:
                if index != 0 and index % 4 == 0:
                    index2 += 1
                if xx == "]":
                    if index2 in basicDict:
                        basicDict[index2].append(x[index-2:index+1])
                    else:
                        basicDict[index2] = x[index-2:index+1]
                        basicDict[index2] = [basicDict[index2]]
                index += 1

        elif x.find("move") != -1:
            move = x.find("move ")
            where = x.find("from ")
            to = x.find("to ")
            move2 = int(x[move+4:x.find(" from")])
            where2 = int(x[where+5:x.find(" to")])-1
            to2 = int(x[to+2:len(x)])-1
            for i in range(0, move2):
                basicDict[to2].insert(0, basicDict[where2].pop(0))
                
sorted_keys = sorted(basicDict.keys())
sortedKeys = {key:basicDict[key] for key in sorted_keys}
boxes = []
for keys in sortedKeys:
    boxes.append(basicDict[keys].pop(0))
sboxes = ' '.join(boxes).replace("[", "").replace("]", "").replace(" ", "")
print(" part 1: " + str(sboxes))

# Part 2

basicDict = {}
with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        if x.find("move") == -1 and x.find("[") != -1:
            index = 0
            index2 = 0
            for xx in x:
                if index != 0 and index % 4 == 0:
                    index2 += 1
                if xx == "]":
                    if index2 in basicDict:
                        basicDict[index2].append(x[index-2:index+1])
                    else:
                        basicDict[index2] = x[index-2:index+1]
                        basicDict[index2] = [basicDict[index2]]
                index += 1
                
        elif x.find("move") != -1:
            move = x.find("move ")
            where = x.find("from ")
            to = x.find("to ")
            move2 = int(x[move+4:x.find(" from")])
            where2 = int(x[where+5:x.find(" to")])-1
            to2 = int(x[to+2:len(x)])-1
            for i in range(0, move2):
                next_move = (move2-1) - i
                basicDict[to2].insert(0, basicDict[where2].pop(next_move))

sorted_keys = sorted(basicDict.keys())
sortedKeys = {key:basicDict[key] for key in sorted_keys}
boxes = []
for keys in sortedKeys:
    boxes.append(basicDict[keys].pop(0))
sboxes = ' '.join(boxes).replace("[", "").replace("]", "").replace(" ", "")
print(" part 2: " + sboxes)