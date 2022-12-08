# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:07:48 2022

@author: Esa
"""
import copy
import os
cwd = os.getcwd()
Day = 8
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input

from collections import defaultdict



### Part 1
Sizes = defaultdict(int)
trees = []

index1 = 0
index2 = 0

with open(selectedInput) as f:
    index1 = 0
    for i in f:
        x = i.rstrip()
        index2 = 0
        for j in x:
            index2 += 1
        index1 += 1

temptrees = []

with open(selectedInput) as f:
    for i in f:
        x = i.rstrip()
        temptrees = []
        for j in x:
            temptrees.append(int(j))
        trees.append(temptrees)

trees2 = copy.deepcopy(trees)
treecount = 0

for i in range(len(trees)):
    for j in range(len(trees[0])):
        if i == 0 or j == 0 or i == index1-1 or j == index2-1:
            treecount += 1
        elif int(trees[i][j]) > int(max(trees[i][0:j])):
            treecount += 1
        elif int(trees[i][j]) > int(max(trees[i][j+1:index2])):
            treecount += 1
        elif int(trees[i][j]) > int(max([trees[-k][j] for k in range(1,int(len(trees)+1))][0:(index1-1-i)])):
            treecount += 1
        elif int(trees[i][j]) > int(max([trees[k][j] for k in range(int(len(trees)))][0:i])):
            treecount += 1
print("Part1: " + str(treecount))

### Part 2

trees3 = copy.deepcopy(trees)
treescore = 0
scenicscore = [0, 0, 0, 0]

for i in range(len(trees)):
    for j in range(len(trees[i])):
        
        for z in range(j-1,-1,-1):
            if j > 0 and trees[i][j] > trees[i][z]:
                scenicscore[0] += 1
            elif j > 0 and trees[i][j] <= trees[i][z]:
                scenicscore[0] += 1
                break
            else:
                break

        for c in range(j+1,len(trees[i]),1):
            if j < len(trees[i])-1 and trees[i][j] > trees[i][c]:
                scenicscore[1] += 1
            elif j < len(trees[i])-1 and trees[i][j] <= trees[i][c]:
                scenicscore[1] += 1
                break
            else:
                break

        for v in range(i-1,-1,-1):
            if i > 0 and trees[i][j] > trees[v][j]:
                scenicscore[2] += 1
            elif i > 0 and trees[i][j] <= trees[v][j]:
                scenicscore[2] += 1
                break
            else:
                break

        for b in range(i+1,len(trees),1):
            if i < len(trees)-1 and trees[i][j] > trees[b][j]:
                scenicscore[3] += 1
            elif i < len(trees)-1 and trees[i][j] <= trees[b][j]:
                scenicscore[3] += 1
                break
            else:
                break
        multi = 1
        for x in scenicscore:
            multi = multi * int(x)
            finalscore = multi
        trees3[i][j] = finalscore
        if finalscore > treescore:
            treescore = finalscore
        scenicscore = [0, 0, 0, 0]

print("Part2: " + str(treescore))