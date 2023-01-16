# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 13:12:17 2022

Description
-----------
Advent of Code
Day 4: Camp Cleanup Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

def overlaps(I, J):
    return not (I[1] < J[0] or J[1] < I[0])

count = 0

for line in open("Day 4 Camp Cleanup.txt", "r"):
    if line == "\n":
        continue
    
    pair_sections = line.rstrip("\n").split(",")
    pair_ends = [[int(end) for end in sections.split("-")] for sections in pair_sections]
    
    if overlaps(pair_ends[0], pair_ends[1]):
        count += 1
        
print(count)