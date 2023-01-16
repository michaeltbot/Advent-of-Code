# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 17:10:55 2022

Description
-----------
Advent of Code
Day 12: Hill Climbing Algorithm Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

with open("Day 12 Hill Climbing Algorithm.txt", "r") as f:
    grid_letter = np.array([list(l) for l in f.read().rstrip("\n").split("\n")])
    grid = np.zeros(grid_letter.shape)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid_letter[i, j] == "S":
                start = (i, j)
                grid[i, j] = 1
            elif grid_letter[i, j] == "E":
                end = (i, j)
                grid[i, j] = 26
            else:
                grid[i, j] = ord(grid_letter[i, j]) - ord('a') + 1
                
fewest_steps = np.full(shape=grid.shape, fill_value = np.inf)
current_positions = [end]
steps = 0
while all(grid[pos] > 1 for pos in current_positions):
    new_positions = []
    steps += 1
    for pos in current_positions:
        for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            try:
                next_pos = (pos[0] + step[0], pos[1] + step[1])
                if grid[next_pos] + 1 >= grid[pos] and steps < fewest_steps[next_pos]:
                    fewest_steps[next_pos] = steps
                    new_positions.append(next_pos)
            except IndexError:
                pass
    current_positions = new_positions
    
print(steps)