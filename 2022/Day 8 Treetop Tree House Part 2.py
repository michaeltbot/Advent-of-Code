# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 13:08:54 2022

Description
-----------
Advent of Code
Day 8: Treetop Tree House Part 2
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

def viewing_distance(grid, x, y, i, j):
    u, v = x + i, y + j
    count = 0
    while 0 <= u < len(grid) and 0 <= v < len(grid):
        count += 1
        if grid[u, v] >= grid[x, y]:
            break
        else:
            u += i
            v += j
    return count

def scenic_score(grid, x, y):
    score = 1
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        score *= viewing_distance(grid, x, y, i, j)
    return score

with open("Day 8 Treetop Tree House.txt") as f:
    lines = f.read().splitlines()
    grid = np.array([[int(x) for x in l] for l in lines])
    
highest_score = 0
for x in range(len(grid)):
    for y in range(len(grid)):
        highest_score = max(highest_score, scenic_score(grid, x, y))

print(highest_score)
