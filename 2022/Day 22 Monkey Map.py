import re
import numpy  as np

with open("Day 22 Monkey Map.txt", "r") as f:
    map_data, path_data = f.read().split("\n\n")

map = np.array([list(line.ljust(150)) for line in map_data.split("\n")])

path_data = path_data.rstrip("\n")
path = [x if x == "L" or x == "R" else int(x) for x in re.split(r'([LR])', path_data)]

direction = [np.array((0, 1)), np.array((1, 0)), np.array((0, -1)), np.array((-1, 0))]

position = np.array((0, min(col for col in range(map.shape[1]) if map[0, col] != ' ')))
facing = 0

for step in path:
    if step == "L":
        facing -= 1
        facing %= 4
        continue
    if step == "R":
        facing += 1
        facing %= 4
        continue

    d = direction[facing]
    for i in range(step):
        next_position = (position + d) % map.shape

        while map[next_position[0], next_position[1]] == ' ':
            next_position = (next_position + d) % map.shape

        if map[next_position[0], next_position[1]] == ".":
            position = next_position
        else:
            break

result = 1000*(position[0]+1) + 4*(position[1]+1) + facing
print(result)
