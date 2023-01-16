import numpy as np

cubes = []
with open("Day 18 Boiling Boulders.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip("\n")
        coords = tuple(int(x) for x in line.split(","))
        cubes.append(coords)

max_coord = tuple(max(cube[i] for cube in cubes) + 1 for i in range(3))
grid = np.full(max_coord, False, dtype=bool)

for cube in cubes:
    grid[cube] = True

total = 0
for cube in cubes:
    for i in range(3):
        position = tuple(cube[j] + int(j==i) for j in range(3))
        if position[i] == max_coord[i] or (not grid[position]):
            total += 1
        position = tuple(cube[j] - int(j==i) for j in range(3))
        if position[i] < 0 or (not grid[position]):
            total += 1

print(total)

# 3D representation of droplet
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(grid)
plt.show()