import numpy as np

def display(elves):
    min_row = min(i for i, j in elves)
    min_col = min(j for i, j in elves)
    normalised_elves = [(i - min_row, j - min_col) for i, j in elves]

    rows = max(i for i, j in normalised_elves) + 1
    cols = max(j for i, j in normalised_elves) + 1

    grid = np.full((rows, cols), '.')
    for i, j in normalised_elves:
        grid[i, j] = '#'

    string = "\n".join("".join(grid[i]) for i in range(grid.shape[0]))
    print(string)

def check_direction(elves, i, j, direction):
    if direction == "N":
        return all((i - 1, j + d) not in elves for d in [-1, 0, 1])
    elif direction == "E":
        return all((i + d, j + 1) not in elves for d in [-1, 0, 1])
    elif direction == "S":
        return all((i + 1, j + d) not in elves for d in [-1, 0, 1])
    elif direction == "W":
        return all((i + d, j - 1) not in elves for d in [-1, 0, 1])

compass = ['N', 'S', 'W', 'E']
direction_vector = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

with open("Day 23 Unstable Diffusion.txt", "r") as f:
    grid = np.array([list(line.rstrip("\n")) for line in f if line != "\n"])

elves = {(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i, j] == '#'}

for n in range(10):
    proposed = dict()
    proposed_count = dict()

    for i, j in elves:
        if all((a, b) not in elves for a in range(i-1, i+2) for b in range(j-1, j+2) if (a, b) != (i, j)):
            continue

        for d in range(n, n + 4):
            direction = compass[d % 4]
            if check_direction(elves, i, j, direction):
                v = direction_vector[direction]
                p = (i + v[0], j + v[1])
                proposed[(i, j)] = p
                proposed_count[p] = proposed_count.get(p, 0) + 1
                break
    
    for pos, next_pos in proposed.items():
        if proposed_count[next_pos] == 1:
            elves.remove(pos)
            elves.add(next_pos)

height = max(i for i, j in elves) - min(i for i, j in elves) + 1
width = max(j for i, j in elves) - min(j for i, j in elves) + 1

empty = width*height - len(elves)
print(empty)

display(elves)