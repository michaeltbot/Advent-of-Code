# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 13:12:17 2022

Description
-----------
Advent of Code
Day 4: Camp Cleanup
"""

import numpy as np
import matplotlib.pyplot as plt

def is_contained(I, J):
    return I[0] >= J[0] and I[1] <= J[1]

count = 0

for line in open("Day 4 Camp Cleanup.txt", "r"):
    if line == "\n":
        continue
    
    pair_sections = line.rstrip("\n").split(",")
    pair_ends = [[int(end) for end in sections.split("-")] for sections in pair_sections]
    
    if is_contained(pair_ends[0], pair_ends[1]) or is_contained(pair_ends[1], pair_ends[0]):
        count += 1
        
print(count)