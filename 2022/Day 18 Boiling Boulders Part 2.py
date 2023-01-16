import numpy as np
import matplotlib.pyplot as plt

cubes = []
with open("Day 18 Boiling Boulders.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip("\n")
        coords = tuple(int(x) for x in line.split(","))
        cubes.append(coords)

max_coord = tuple(max(cube[i] for cube in cubes) + 1 for i in range(3))
grid = np.zeros(max_coord, dtype=np.int8)

grid[0, :, :] = np.ones((max_coord[1], max_coord[2]))
grid[-1, :, :] = np.ones((max_coord[1], max_coord[2]))

grid[:, 0, :] = np.ones((max_coord[0], max_coord[2]))
grid[:, -1, :] = np.ones((max_coord[0], max_coord[2]))

grid[:, :, 0] = np.ones((max_coord[0], max_coord[1]))
grid[:, :, -1] = np.ones((max_coord[0], max_coord[1]))

for cube in cubes:
    grid[cube] = 2

# Flow the "water" (grid = 1) around the droplet, to find what squares aren't enclosed in the droplet
current = {(i, j, k) for i in range(max_coord[0]) for j in range(max_coord[1]) for k in range(max_coord[2]) if grid[i, j, k] == 1}
while len(current) > 0:
    new = set()
    for cube in current:
        for i in range(3):
            position = tuple(cube[j] + int(j==i) for j in range(3))
            if position[i] < max_coord[i] and grid[position] == 0:
                grid[position] = 1
                new.add(position)
            position = tuple(cube[j] - int(j==i) for j in range(3))
            if position[i] > 0 and grid[position] == 0:
                grid[position] = 1
                new.add(position)
    current = new


total = 0
for cube in cubes:
    for i in range(3):
        position = tuple(cube[j] + int(j==i) for j in range(3))
        if position[i] == max_coord[i] or grid[position] == 1:
            total += 1
        position = tuple(cube[j] - int(j==i) for j in range(3))
        if position[i] < 0 or grid[position] == 1:
            total += 1

print(total)