# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 11:37:25 2022

@author: Esa
"""

import copy
import os
cwd = os.getcwd()
Day = 11
test_input =  cwd + "/test-input-" + str(Day) + ".txt"
real_input =  cwd + "/input-" + str(Day) + ".txt"

from collections import defaultdict
from math import floor
selectedInput = None
test = False

if test:
    selectedInput = test_input
else:
    selectedInput = real_input
    
monkeys = defaultdict(dict)
curMonkey = None
operations = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}
divisible = None
with open(selectedInput) as f:
    for i in f:
            x = i.rstrip().split()
            if len(x) > 0:
                #print(x)
                #print(len(x))
                if x[0] == 'Monkey':
                    curMonkey = x[1].strip(':')
                    monkeys[curMonkey]['items'] = []
                    monkeys[curMonkey]['seen'] = 0
                    monkeys[curMonkey]['divisible'] = None
                    monkeys[curMonkey]['trueMonkey'] = None
                    monkeys[curMonkey]['falseMonkey'] = None
                elif x[1] == 'items:':
                    monkeys[curMonkey]['items'] = [int(k.strip(',')) for k in x[2:]]
                    
                elif x[0] == 'Test:':
                    monkeys[curMonkey]['divisible'] = int(x[3])
                elif x[1] == 'true:':
                    monkeys[curMonkey]['trueMonkey'] = x[-1]
                elif x[1] == 'false:':
                    monkeys[curMonkey]['falseMonkey'] = x[-1]
#for keys in monkeys:
    #print(keys, monkeys[keys])

if test:
    cycles = 20
    for i in range(cycles):
        for keys in monkeys:
            monkeys[keys]['seen'] += len(monkeys[keys]['items'])
            #print(monkeys[keys]['items'])
            if keys == '0':
                #new = operations['*'](old, 19)
                monkeys[keys]['items'] = [operations['*'](k, 19) for k in monkeys[keys]['items']]
            elif keys == '1':
                #new = operations['+'](old, 6)
                monkeys[keys]['items'] = [operations['+'](k, 6) for k in monkeys[keys]['items']]
            elif keys == '2':
                
                #new = operations['*'](old, old)
                monkeys[keys]['items'] = [operations['*'](k, k) for k in monkeys[keys]['items']]
            elif keys == '3':
                #new = operations['+'](old, 3)
                monkeys[keys]['items'] = [operations['+'](k, 3) for k in monkeys[keys]['items']]
            monkeys[keys]['items'] = [floor(operations['/'](k, 3)) for k in monkeys[keys]['items']]
            while len(monkeys[keys]['items']) > 0:
                new = monkeys[keys]['items'].pop(0)
                if new % monkeys[keys]['divisible'] == 0:
                    monkeys[monkeys[keys]['trueMonkey']]['items'].append(new)
                else:
                    monkeys[monkeys[keys]['falseMonkey']]['items'].append(new)
            #monkeys[keys]['items'] = list()
        #for keys2 in monkeys: 
             #print("Round; ", i, monkeys[keys2]['items'])
    #for keys in monkeys:
        #print(keys, monkeys[keys]['seen'])
else:
    cycles = 20
    for i in range(cycles):
        for keys in monkeys:
            monkeys[keys]['seen'] += len(monkeys[keys]['items'])
            
            if keys == '0':
                
                monkeys[keys]['items'] = [operations['*'](k, 11) for k in monkeys[keys]['items']]
            elif keys == '1':
                
                monkeys[keys]['items'] = [operations['*'](k, 17) for k in monkeys[keys]['items']]
            elif keys == '2':
                
                
                monkeys[keys]['items'] = [operations['+'](k, 8) for k in monkeys[keys]['items']]
            elif keys == '3':
                
                monkeys[keys]['items'] = [operations['+'](k, 3) for k in monkeys[keys]['items']]
            elif keys == '4':
                
                monkeys[keys]['items'] = [operations['+'](k, 4) for k in monkeys[keys]['items']]
            elif keys == '5':
                
                monkeys[keys]['items'] = [operations['+'](k, 7) for k in monkeys[keys]['items']]
            elif keys == '6':
                
                monkeys[keys]['items'] = [operations['*'](k, k) for k in monkeys[keys]['items']]
            elif keys == '7':
                
                monkeys[keys]['items'] = [operations['+'](k, 6) for k in monkeys[keys]['items']]
            monkeys[keys]['items'] = [floor(operations['/'](k, 3)) for k in monkeys[keys]['items']]
            while len(monkeys[keys]['items']) != 0:
                new = monkeys[keys]['items'].pop(0)
                if new % monkeys[keys]['divisible'] == 0:
                    monkeys[monkeys[keys]['trueMonkey']]['items'].append(new)
                else:
                    monkeys[monkeys[keys]['falseMonkey']]['items'].append(new)

    seens = list()
    for keys in monkeys:
        seens.append(monkeys[keys]['seen'])
        seens.sort(reverse=True)
print("Part 1: " + str(seens[0]*seens[1]))
        
### Part 2
monkeys = defaultdict(dict)
with open(selectedInput) as f:
    for i in f:
            x = i.rstrip().split()
            if len(x) > 0:

                if x[0] == 'Monkey':
                    curMonkey = x[1].strip(':')
                    monkeys[curMonkey]['items'] = []
                    monkeys[curMonkey]['seen'] = 0
                    monkeys[curMonkey]['divisible'] = None
                    monkeys[curMonkey]['trueMonkey'] = None
                    monkeys[curMonkey]['falseMonkey'] = None
                elif x[1] == 'items:':
                    monkeys[curMonkey]['items'] = [int(k.strip(',')) for k in x[2:]]
                    
                elif x[0] == 'Test:':
                    monkeys[curMonkey]['divisible'] = int(x[3])
                elif x[1] == 'true:':
                    monkeys[curMonkey]['trueMonkey'] = x[-1]
                elif x[1] == 'false:':
                    monkeys[curMonkey]['falseMonkey'] = x[-1]

cycles = 10000
if test:
    for i in range(cycles):
        for keys in monkeys:
            monkeys[keys]['seen'] += len(monkeys[keys]['items'])
            
            lcm = 13*17*19*23
            if keys == '0':
                
                monkeys[keys]['items'] = [operations['*'](k, 19) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '1':
                
                monkeys[keys]['items'] = [operations['+'](k, 6) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '2':
                
               
                monkeys[keys]['items'] = [operations['*'](k, k) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '3':
                
                monkeys[keys]['items'] = [operations['+'](k, 3) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            
            while len(monkeys[keys]['items']) > 0:
                new = monkeys[keys]['items'].pop(0)
                if new % monkeys[keys]['divisible'] == 0:
                    monkeys[monkeys[keys]['trueMonkey']]['items'].append(new)
                else:
                    monkeys[monkeys[keys]['falseMonkey']]['items'].append(new)

    for keys in monkeys:
        print(keys, monkeys[keys]['seen'])
else:
    for i in range(cycles):
        for keys in monkeys:
            monkeys[keys]['seen'] += len(monkeys[keys]['items'])
            lcm = 5*13*7*19*2*11*17*3
            if keys == '0':
                
                monkeys[keys]['items'] = [operations['*'](k, 11) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '1':
                
                monkeys[keys]['items'] = [operations['*'](k, 17) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '2':
                
                
                monkeys[keys]['items'] = [operations['+'](k, 8) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '3':
                
                monkeys[keys]['items'] = [operations['+'](k, 3) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '4':
                
                monkeys[keys]['items'] = [operations['+'](k, 4) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '5':
                
                monkeys[keys]['items'] = [operations['+'](k, 7) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '6':
                
                monkeys[keys]['items'] = [operations['*'](k, k) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]
            elif keys == '7':
                
                monkeys[keys]['items'] = [operations['+'](k, 6) for k in monkeys[keys]['items']]
                monkeys[keys]['items'] = [k % lcm for k in monkeys[keys]['items']]

            while len(monkeys[keys]['items']) != 0:
                new = monkeys[keys]['items'].pop(0)
                if new % monkeys[keys]['divisible'] == 0:
                    monkeys[monkeys[keys]['trueMonkey']]['items'].append(new)
                else:
                    monkeys[monkeys[keys]['falseMonkey']]['items'].append(new)

    seens = list()
    for keys in monkeys:
        seens.append(monkeys[keys]['seen'])
        seens.sort(reverse=True)
    print("Part 2: " + str(seens[0]*seens[1]))