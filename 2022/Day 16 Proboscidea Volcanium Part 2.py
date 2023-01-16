"""
Description
-----------
Advent of Code
Day 16: Proboscidea Volcanium
"""

def shortest_path(adjacent, start):
    unvisited = set(adjacent.keys())
    unvisited.remove(start)
    distances = {start: 0}
    current = [start]
    distance = 0
    while len(unvisited) > 0:
        distance += 1
        new = []
        for node in current:
            for adj in adjacent[node]:
                if adj in unvisited:
                    distances[adj] = distance
                    new.append(adj)
                    unvisited.remove(adj)
        current = new
    return distances

def turn_next_valve(flow_rate, shortest_paths, unvisited, start1, time1, start2, time2):
    if time1 < time2:
        start1, start2 = start2, start1
        time1, time2 = time2, time1

    max_pressure = 0
    for valve in unvisited:
        distance = shortest_paths[start1][valve]
        if distance + 1 < time1:
            new_time = time1 - distance - 1
            new_unvisited = unvisited.difference({valve})
            pressure = turn_next_valve(flow_rate, shortest_paths, new_unvisited, valve, new_time, start2, time2)
            max_pressure = max(max_pressure, flow_rate[valve]*new_time + pressure)
    return max_pressure


flow_rate = dict()
adjacent = dict()

for line in open("Day 16 Proboscidea Volcanium.txt", "r"):
    if line == "\n":
        break
    line = line.rstrip("\n")

    words = line.split(" ")
    valve = words[1]
    flow_rate[valve] = int(words[4][5:-1])
    adjacent[valve] = [w.rstrip(",") for w in words[9:]]

working_valves = [valve for valve in flow_rate if flow_rate[valve] > 0]

shortest_paths = dict()
for valve in ['AA'] + working_valves:
    distances = shortest_path(adjacent, valve)
    shortest_paths[valve] = {v: d for v, d in distances.items() if v in working_valves}

t = 26
max_pressure = turn_next_valve(flow_rate, shortest_paths, set(working_valves), 'AA', t, 'AA', t)
print(max_pressure)