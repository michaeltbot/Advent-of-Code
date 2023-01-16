# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 13:08:54 2022

Description
-----------
Advent of Code
Day 8: Treetop Tree House
"""

import numpy as np
import matplotlib.pyplot as plt

def visibles_from_front(line):
    visibles_line = np.zeros(len(line))
    tallest = -1
    for i in range(len(line)):
        if line[i] > tallest:
            visibles_line[i] = 1
            tallest = line[i]
    return visibles_line

def visibles_in_line(line):
    return visibles_from_front(line) + visibles_from_front(line[::-1])[::-1]
    
def visibles(grid):
    visible = np.array([visibles_in_line(l) for l in grid])
    visible += np.array([visibles_in_line(l) for l in grid.T]).T
    return visible

with open("Day 8 Treetop Tree House.txt") as f:
    lines = f.read().splitlines()
    grid = np.array([[int(x) for x in l] for l in lines])
    
print(np.count_nonzero(visibles(grid)))