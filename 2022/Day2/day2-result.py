# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:36:16 2022

@author: Esa
"""

""" AOC 2022 Day 2
"""
import os
cwd = os.getcwd()
Day = 2
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"


"""
Part 1

A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors

"""

selectedInput = None

Opponent = None
Self = None
first = None
second = None

shapeScore = 0
runningScore = 0
finalScore = 0
roundScore = 0

test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
with open(selectedInput) as f:
        for i in f:
            x = i.rstrip().split(" ")
            #print(x)
            roundScore = 0
            first = ord(x[0])-64
            second = ord(x[1])-87
            roundScore = second
            result = first - second
            if result == 0:
                roundScore = roundScore + 3
            elif result == -1 or result == 2:
                roundScore = roundScore + 6
            elif result < -1:
                roundScore = roundScore + 0
            #print(roundScore)
            runningScore = runningScore + roundScore
finalScore = runningScore
#print(shapeScore)
#print(winScore)
print("part1 " + str(finalScore))
                
# else:
#     with open(real_input) as f:
#         for i in f:
#             x = i.rstrip().split(" ")
#             #print(x)
#             roundScore = 0
#             first = ord(x[0])-64
#             second = ord(x[1])-87
#             roundScore = second
#             result = first - second
#             if result == 0:
#                 roundScore = roundScore + 3
#             elif result == -1 or result == 2:
#                 roundScore = roundScore + 6
#             elif result < -1:
#                 roundScore = roundScore + 0
#             #print(roundScore)
#             runningScore = runningScore + roundScore 
#     finalScore = runningScore
#     #print(shapeScore)
#     #print(winScore)
#     print("part1 " + str(finalScore))


"""
Part 2

A = Rock
B = Paper
C = Scissors

X = Lose
Y = Draw
Z = Win

"""
Opponent = None
Self = None
first = None
second = None

shapeScore = 0
runningScore = 0
finalScore = 0
roundScore = 0

if test:
    selectedInput = test_input
else:
    selectedInput = real_input

with open(selectedInput) as f:
        for i in f:
            x = i.rstrip().split(" ")
            #print(x)
            roundScore = 0
            first = ord(x[0])-64
            second = ord(x[1])-87
            #roundScore = second
            result = second
            if result == 2:
                roundScore = roundScore + 3 + first
            elif result == 3:
                roundScore = roundScore + 6
                if first == 1:
                    roundScore = roundScore + 2
                elif first == 2:
                    roundScore = roundScore + 3
                elif first == 3:
                    roundScore = roundScore + 1    
            elif result == 1:
                roundScore = roundScore + 0
                if first == 1:
                    roundScore = roundScore + 3
                elif first == 2:
                    roundScore = roundScore + 1
                elif first == 3:
                    roundScore = roundScore + 2   
            #print(roundScore)
            runningScore = runningScore + roundScore
finalScore = runningScore
#print(shapeScore)
#print(winScore)
print("part2 " + str(finalScore))
                
