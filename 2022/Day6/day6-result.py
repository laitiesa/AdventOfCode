# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:47:13 2022

@author: Esa
"""

import os
user = os.path.expanduser('~')
AoCDir = "/OneDrive/Tiedostot/AdventOfCode/2022/Day"
Day = 6
test_input =  user + AoCDir + str(Day) + "/test-input-" + str(Day) + ".txt"
real_input =  user + AoCDir + str(Day) + "/input-" + str(Day) + ".txt"

#from copy import deepcopy
selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
# Part 1 & 2

S1 = None ## Part 1
S2 = None ## Part 2
with open(selectedInput) as f:
    for i in f:
        for k in range(0,len(i),1):
            if k >= 4:
                S1 = set(i[k-4:k])
                if len(S1) == 4:
                    print("Part 1: " + str(k))
                    break
        for k in range(0,len(i),1):
            if k >= 14:
                S2 = set(i[k-14:k])
                if len(S2) == 14:
                    print("Part 2: " + str(k))
                    break
                