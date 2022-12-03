# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:19:56 2022

@author: Esa
"""

import os
user = os.path.expanduser('~')
AoCDir = "/OneDrive/Tiedostot/AoC2022/2022/Day"
Day = 3

test_input =  user + AoCDir + str(Day) + "/test-input-" + str(Day) + ".txt"
real_input =  user + AoCDir + str(Day) + "/input-" + str(Day) + ".txt"


selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
# Part 1

totalScore = 0 
with open(selectedInput) as f:
        for i in f:
            x = i.rstrip()
            half = int(len(x)/2)
            score = 0
            y = x[0:half]
            z = x[half:]
            #print(x,y,z)
            for char in y:
                count = z.count(char)
                if count > 0:
                    if char.islower():
                        score = ord(char)-96
                    else:
                        score = ord(char)-38
                    totalScore += score
                    #print(char, count, score)
                    break
            #print(ord("a")-96, ord("z")-96,ord("A")-38,ord("Z")-38)
            #print(score)
print("Part1 " + str(totalScore))


# Part 2

totalScore = 0

XS = [str(x.rstrip()) for x in open(selectedInput)]
#print(XS)
for i in range(2,len(XS),3):
        #print(XS[i-2], XS[i-1], XS[i])
        for char in XS[i]:
            count1 = XS[i-1].count(char)
            count2 = XS[i-2].count(char)
            if count1 > 0 and count2 > 0:
                #print(char, count, score)
                if char.islower():
                    score = ord(char)-96
                else:
                    score = ord(char)-38
                totalScore += score
                break
print("Part2 " + str(totalScore))
