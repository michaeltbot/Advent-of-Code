# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 17:10:55 2022

Description
-----------
Advent of Code
Day 12: Hill Climbing Algorithm
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
fewest_steps[start] = 0
current_positions = [start]
steps = 0
while fewest_steps[end] == np.inf:
    new_positions = []
    steps += 1
    for pos in current_positions:
        for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            try:
                next_pos = (pos[0] + step[0], pos[1] + step[1])
                if grid[next_pos] <= grid[pos] + 1 and steps < fewest_steps[next_pos]:
                    fewest_steps[next_pos] = steps
                    new_positions.append(next_pos)
            except IndexError:
                pass
    current_positions = new_positions

# with open("Day 12 Hill Climbing Algorithm Fewest Steps.txt", "w") as f:
#     f.write("\n".join(" ".join(str(int(x)).rjust(3, "0") for x in line) for line in fewest_steps))

path = [end]
position = end
for steps in range(int(fewest_steps[end])-1, -1, -1):
    for step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            prev_position = (position[0] + step[0], position[1] + step[1])
            if fewest_steps[prev_position] == steps:
                path.append(prev_position)
                position = prev_position
                continue
        except IndexError:
            pass
        
path.reverse()

X = np.arange(0, grid.shape[1])
Y = np.arange(0, grid.shape[0])
X, Y = np.meshgrid(X, Y)
levels = np.linspace(np.min(grid), np.max(grid), 15)

fig, ax = plt.subplots()

ax.contourf(X, Y, grid, levels=levels)
ax.plot([p[1] for p in path], [p[0] for p in path], color='red')

plt.show()