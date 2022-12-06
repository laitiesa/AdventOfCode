# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:29:27 2022

@author: Esa
"""

""" AOC 2022 Day 1
"""
import os
cwd = os.getcwd()
Day = 1
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"
"""
Part 1
"""
max_sum = 0
temp_sum = 0


test = False

if test:
    with open(test_input) as f:
        for i in f:
            if i == '\n' or i == '':
                if temp_sum > max_sum:
                    max_sum = temp_sum
                temp_sum = 0
            else:
                    temp_sum = temp_sum + int(i)
                    #print(int(i))
    if temp_sum > max_sum:
        max_sum = temp_sum
    print("Part 1 test result is: " + str(max_sum))

if not test:
    with open(real_input) as f:
        for i in f:
            if i == '\n' or i == '':
                if temp_sum > max_sum:
                    max_sum = temp_sum
                temp_sum = 0
            else:
                temp_sum = temp_sum + int(i)
                #print(int(i))
    if temp_sum > max_sum:
        max_sum = temp_sum
    print("Part 1  real input result is: " + str(max_sum))
    
    
"""
Part 2
"""
list1 = [0, 0, 0]
temp_sum = 0


test = False

if test:
    with open(test_input) as f:
        for i in f:
            if i == '\n' or i == '':
                #print(temp_sum)
                for j in list1:
                    if temp_sum > j:
                        list1.pop(0)
                        list1.append(temp_sum)
                        list1.sort()
                        break
                temp_sum = 0
            else:
                    temp_sum = temp_sum + int(i)
                    #print(int(i))
                    #print(temp_sum)
    for j in list1:
        if temp_sum > j:
            list1.pop(0)
            list1.append(temp_sum)
            list1.sort()
            break
    print("Part 2 test result list is: " + str(list1) + " and sum is: " + str(sum(list1)))

if not test:
    with open(real_input) as f:
        for i in f:
            if i == '\n' or i == '':
                #print(temp_sum)
                for j in list1:
                    if temp_sum > j:
                        list1.pop(0)
                        list1.append(temp_sum)
                        list1.sort()
                        break
                temp_sum = 0
            else:
                    temp_sum = temp_sum + int(i)
                    #print(int(i))
                    #print(temp_sum)
    for j in list1:
        if temp_sum > j:
            list1.pop(0)
            list1.append(temp_sum)
            list1.sort()
            break
    print("Part 2 real result list is: " + str(list1) + " and sum is: " + str(sum(list1)))