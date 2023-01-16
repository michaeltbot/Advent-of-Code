# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 14:38:24 2022

Description
-----------
Advent of Code
Day 10: Cathode-Ray Tube
"""

import numpy as np
import matplotlib.pyplot as plt

total = 0

cycle = 1
X = 1
adding = False
for line in open("Day 10 Cathode-Ray Tube.txt", "r"):
    if line == "\n":
        break
    line = line.rstrip("\n")
    
    if cycle % 40 == 20:
        total += X*cycle
    cycle += 1
    
    if line == "noop":
        continue
    
    instruction, num = line.split(" ")
    if cycle % 40 == 20:
        total += X*cycle
    X += int(num)
    cycle += 1
    
print(total)