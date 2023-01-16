import numpy as np

"""
     7
     ^
     |
5 <- 1 -> 2
     |
     V
     3
"""

num = {".": 1, ">": 2, "v": 3, "<": 5, "^": 7, "#": 0}
char = {2: ">", 3: "v", 5: "<", 7: "^"}

def display(grid):
    s = "#." + "#"*grid.shape[1] + "\n"
    for i in range(grid.shape[0]):
        l = ""
        for j in range(grid.shape[1]):
            n = grid[i, j]
            if n == 1:
                l += "."
                continue
            count = sum(int(n % d == 0) for d in char.keys())
            if count == 1:
                l += char[n]
            else:
                l += str(count)
        s += ("#" + l + "#\n")
    s += "#"*grid.shape[1] + ".#"
    print(s)

def move_blizzard(grid):
    new_grid = np.ones(grid.shape)
    h, w = grid.shape
    for i in range(h):
        for j in range(w):
            n = grid[i, j]
            if n % num[">"] == 0:
                new_grid[i, (j+1)%w] *= num[">"]
            if n % num["v"] == 0:
                new_grid[(i+1)%h, j] *= num["v"]
            if n % num["<"] == 0:
                new_grid[i, (j-1)%w] *= num["<"]
            if n % num["^"] == 0:
                new_grid[(i-1)%h, j] *= num["^"]
    return new_grid

def trip(grid, start, end):
    positions = set()
    minute = 0
    while end not in positions:
        minute += 1
        grid = move_blizzard(grid)
        next_positions = set()
        if grid[start] == 1:
            next_positions.add(start)
        for p in positions:
            if grid[p] == 1:
                next_positions.add(p)
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                q = (p[0]+i, p[1]+j)
                if 0 <= q[0] < grid.shape[0] and 0 <= q[1] < grid.shape[1] and grid[q] == 1:
                    next_positions.add(q)
        positions = next_positions
    grid = move_blizzard(grid)
    return grid, minute + 1

with open("Day 24 Blizzard Basin.txt", "r") as f:
    grid = np.array([[num[s] for s in line.rstrip("\n")] for line in f if line != "\n"])
    grid = grid[1:-1, 1:-1]

start = (0, 0)
end = (grid.shape[0] - 1, grid.shape[1] - 1)

grid, time1 = trip(grid, start, end)
grid, time2 = trip(grid, end, start)
grid, time3 = trip(grid, start, end)

print(time1 + time2 + time3)