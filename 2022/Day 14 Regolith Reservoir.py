# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Sat Dec 17 16:05:26 2022

Description
-----------
Advent of Code
Day 14: Regolith Reservoir
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

import imageio

def create_frame(grid, t):
    fig, ax = plt.subplots()

    cmap = mpl.colors.ListedColormap(['dimgrey', 'tan', 'saddlebrown'])
    ax.imshow(grid.T, cmap=cmap, interpolation='none')

    plt.savefig(f'./img/day14/img_{t}.png', transparent = False, facecolor = 'white')
    
    plt.close(fig)


def plot_cave(grid): 
    fig, ax = plt.subplots()

    cmap = mpl.colors.ListedColormap(['dimgrey', 'tan', 'saddlebrown'])
    ax.imshow(grid.T, cmap=cmap, interpolation='none')

    plt.show()

def fall(grid, start):
    sand = (start, 0)
    while sand[1] < grid.shape[1] - 1:
        if grid[sand[0], sand[1] + 1] == 0:
            sand = (sand[0], sand[1] + 1)
        elif grid[sand[0] - 1, sand[1] + 1] == 0:
            sand = (sand[0] - 1, sand[1] + 1)
        elif grid[sand[0] + 1, sand[1] + 1] == 0:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            grid[sand] = 0.5
            return True
    return False

structures = []
with open("Day 14 Regolith Reservoir.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip("\n")
        
        struct = [tuple(int(x) for x in coord.split(",")) for coord in line.split(" -> ")]
        structures.append(struct)
        
min_x = min(p[0] for struct in structures for p in struct)
max_x = max(p[0] for struct in structures for p in struct)
max_y = max(p[1] for struct in structures for p in struct)

structures = [[(p[0] - min_x, p[1]) for p in struct] for struct in structures]
start = 500 - min_x

width = max_x - min_x + 1
height = max_y + 1

grid = np.zeros((width, height))
for struct in structures:
    for i in range(len(struct) - 1):
        if struct[i][0] == struct[i+1][0]:
            if struct[i][1] < struct[i+1][1]:
                step = 1
            else:
                step = -1
            for y in range(struct[i][1], struct[i+1][1], step):
                grid[struct[i][0], y] = 1
        else:
            if struct[i][0] < struct[i+1][0]:
                step = 1    
            else:
                step = -1
            for x in range(struct[i][0], struct[i+1][0], step):
                grid[x, struct[i][1]] = 1
    grid[struct[-1]] = 1
    
units = 0
create_frame(grid, 0)
while fall(grid, start):
    units += 1
    # create_frame(grid, units)
    
print(units)

plot_cave(grid)
# %%
import imageio
units = 961

frames = []
for t in range(0, units+1, 3):
    image = imageio.v2.imread(f'./img/day14/img_{t}.png')
    frames.append(image)
    
imageio.mimwrite('./Day 14 Regolith Reservoir Timelapse Faster.gif', frames, fps=60)