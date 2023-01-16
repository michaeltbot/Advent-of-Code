import re
import numpy  as np
import itertools as it

direction = [np.array((0, 1)), np.array((1, 0)), np.array((0, -1)), np.array((-1, 0))]

def find_connections(map, length):
    net = np.array([[map[i, j] != ' ' for  j in range(0, map.shape[1], length)] for i in range(0, map.shape[0], length)])
    corners = np.zeros(map.shape + (2, 2, 3), dtype=int)

    start = min(j for j in range(net.shape[1]) if net[0, j])
    corners[0, start, :, :, :] = np.array([[[0, 0, 0], [0, 1, 0]], [[1, 0, 0], [1, 1, 0]]])

    remaining = {(i, j) for i in range(net.shape[0]) for j in range(net.shape[1]) if net[i, j]}
    current = {(0, start)}
    remaining.remove((0, start))
    while len(remaining) > 0:
        next_current = set()
        for pos in current:
            for facing in range(4):
                d = direction[facing]
                p = (pos[0] + d[0], pos[1] + d[1])
                if p in remaining:
                    if facing == 0:
                        top = [(0, 1), (1, 1)]
                        bottom = [(0, 0), (1, 0)]
                    elif facing == 1:
                        top = [(1, 0), (1, 1)]
                        bottom = [(0, 0), (0, 1)]
                    elif facing == 2:
                        top = [(0, 0), (1, 0)]
                        bottom = [(0, 1), (1, 1)]
                    elif facing == 3:
                        top = [(0, 0), (0, 1)]
                        bottom = [(1, 0), (1, 1)]

                    x, y = pos
                    difference = np.array([int(corners[x, y, top[0][0], top[0][1], k] == corners[x, y, bottom[1][0], bottom[1][1], k]) for k in range(3)])

                    for k in range(2):
                        corners[p[0], p[1], bottom[k][0], bottom[k][1], :] = corners[x, y, top[k][0], top[k][1], :]
                        corners[p[0], p[1], top[k][0], top[k][1], :] = (corners[x, y, top[k][0], top[k][1], :] + difference) % 2
                    
                    next_current.add(p)
                    remaining.remove(p)
        current = next_current
    
    reverse_side = dict()
    for i in range(net.shape[0]):
        for j in range(net.shape[1]):
            if net[i, j]:
                for d in range(4):
                    l = []
                    if d == 0 or d == 1:
                        l.append(tuple(corners[i, j, 1, 1]))
                    if d == 1 or d == 2:
                        l.append(tuple(corners[i, j, 1, 0]))
                    if d == 2 or d == 3:
                        l.append(tuple(corners[i, j, 0, 0]))
                    if d == 3 or d == 0:
                        l.append(tuple(corners[i, j, 0, 1]))
                    t = tuple(sorted(l))
                    
                    try:
                        reverse_side[t].add((i, j, d))
                    except KeyError:
                        reverse_side[t] = {(i, j, d)}

    connected_side = np.zeros(net.shape + (4, 3), dtype=int)
    for s1, s2 in reverse_side.values():
        connected_side[s1] = np.array(s2)
        connected_side[s2] = np.array(s1)
    
    return connected_side

def move(map, connected_side, position, facing):
    length = map.shape[0] // connected_side.shape[0]
    p = position + direction[facing]
    if 0 <= p[0] < map.shape[0] and 0 <= p[1] < map.shape[1] and map[p[0], p[1]] != ' ':
        return p, facing

    row, col = position // length
    r, c, f = connected_side[row, col, facing]

    if facing == 0:
        distance = position[0] % length
    elif facing == 1:
        distance = (length - 1 - position[1]) % length
    elif facing == 2:
        distance = (length - 1 - position[0]) % length
    else:
        distance = position[1] % length

    p = np.array([r*length, c*length])
    if f == 0:
        p[0] += (length - 1 - distance)
        p[1] += (length - 1)
    elif f == 1:
        p[0] += (length - 1)
        p[1] += distance
    elif f == 2:
        p[0] += distance
    else:
        p[1] += (length - 1 - distance)
    
    return p, (f + 2) % 4

with open("Day 22 Monkey Map.txt", "r") as f:
    map_data, path_data = f.read().split("\n\n")

width = max(len(line) for line in map_data.split("\n"))
map = np.array([list(line.ljust(width)) for line in map_data.split("\n")])
length = 50

connected_side = find_connections(map, length)

path_data = path_data.rstrip("\n")
path = [x if x == "L" or x == "R" else int(x) for x in re.split(r'([LR])', path_data)]

position = np.array((0, min(col for col in range(map.shape[1]) if map[0, col] != ' ')))
facing = 0

map[position[0], position[1]] = [">", "v", "<", "^"][facing]

for step in path:
    if step == "L":
        facing -= 1
        facing %= 4
        map[position[0], position[1]] = [">", "v", "<", "^"][facing]
        continue
    if step == "R":
        facing += 1
        facing %= 4
        map[position[0], position[1]] = [">", "v", "<", "^"][facing]
        continue

    for i in range(step):
        next_position, next_facing = move(map, connected_side, position, facing)

        if map[next_position[0], next_position[1]] == "#":
            break
        else:
            position = next_position
            facing = next_facing
            map[position[0], position[1]] = [">", "v", "<", "^"][facing]

with open("Day 22 Result Map.txt", "w") as f:
    f.write("\n".join("".join(map[i, :]) for i in range(map.shape[0])))

result = 1000*(position[0]+1) + 4*(position[1]+1) + facing
print(result)