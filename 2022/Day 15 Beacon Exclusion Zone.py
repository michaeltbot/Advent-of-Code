"""
Description
-----------
Advent of Code
Day 15: Beacon Exclusion Zone
"""

sensor_beacon = dict()
with open("Day 15 Beacon Exclusion Zone.txt", "r") as f:
    for line in f:
        if line == "\n":
            break
        line = line.rstrip("\n")

        x_s = int(line[line.find("x=")+2: line.find(",")])
        y_s = int(line[line.find("y=")+2: line.find(":")])

        x_b = int(line[line.rfind("x=")+2: line.rfind(",")])
        y_b = int(line[line.rfind("y=")+2:])

        sensor_beacon[(x_s, y_s)] = (x_b, y_b)

y = 2000000

no_beacon_ranges = []

for sensor, beacon in sensor_beacon.items():
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    distance_to_y = abs(sensor[1] - y)
    if distance > distance_to_y:
        x = distance - distance_to_y
        no_beacon_ranges.append((sensor[0] - x, sensor[0] + x))

no_beacon_ranges.sort()
new_ranges = [no_beacon_ranges[0]]
for x1, x2 in no_beacon_ranges[1:]:
    y1, y2 = new_ranges[-1]
    if y2 >= x1:
        new_ranges[-1] = (y1, max(x2, y2))
    else:
        new_ranges.append((x1, x2))

total = 0
for x1, x2 in new_ranges:
    total += (x2 - x1 + 1)

for x_b, y_b in set(sensor_beacon.values()):
    if y_b == y:
        for x1, x2 in new_ranges:
            if x1 <= x_b <= x2:
                total -= 1
                break

print(total)
print(no_beacon_ranges)
print(new_ranges)