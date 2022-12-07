# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:07:48 2022

@author: Esa
"""

import os
cwd = os.getcwd()
Day = 7
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input

from collections import defaultdict

Sizes = defaultdict(int)
directory = []

with open(selectedInput) as f:
    for i in f:
        x = i.split()
        if x[1] == 'cd' and x[2] != '..':
            directory.append(x[2])
        if x[1] == 'cd' and x[2] == '..':
             directory.pop()
        else:
            try:
                size = int(x[0])
                for y in range(len(directory)+1):
                    Sizes['/'.join(directory[:y])] += size
            except:
                pass
sums = 0

for i,j in Sizes.items():
    if j <= 100000:
        sums += j
print("Part 1: " + str(sums))

total_space = 70000000
min_space = 30000000
max_cap = total_space - min_space
suit_dir = None
suit_dir_size = 30000000
cur_space = Sizes['/']
for i,j in Sizes.items():
    if (cur_space - j) <= max_cap and (j < suit_dir_size):
        suit_dir, suit_dir_size = i, j
        
print("Part 1: " + suit_dir, str(Sizes[suit_dir]))