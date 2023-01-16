# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 14:14:46 2022

Description
-----------
Advent of Code
Day 5: Supply Stacks Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

stacks = {n: [] for n in range(1, 10)}

f = open("Day 5 Supply Stacks.txt", "r")
for line in f:
    if line == "\n":
        break
    line = line.rstrip("\n")
    
    n = 1
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[n].append(line[i])
        n += 1
        
for n in range(1, 10):
    stacks[n].pop()
    stacks[n].reverse()

for line in f:
    if line == "\n":
        break
    
    for s in ["move ", " from ", " to ", "\n"]:
        line = line.replace(s, ",")
        
    amount, start, end = [int(x) for x in line.split(",") if x != '']
    
    picked_up = []
    for i in range(amount):
        picked_up.append(stacks[start].pop())
    picked_up.reverse()
    stacks[end].extend(picked_up)
        
tops = "".join(stacks[n][-1] for n in range(1, 10))
print(tops)