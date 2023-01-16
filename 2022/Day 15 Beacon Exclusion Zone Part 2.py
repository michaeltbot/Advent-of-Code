"""
Description
-----------
Advent of Code
Day 15: Beacon Exclusion Zone Part 2
"""

import matplotlib.pyplot as plt

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

width = 4000000

no_beacon_areas = []

for sensor, beacon in sensor_beacon.items():
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    corners = []
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        corners.append((sensor[0] + distance*x, sensor[1] + distance*y))
    no_beacon_areas.append(corners)

# negative_lines = dict()
# positive_lines = dict()
# for i in range(len(no_beacon_areas)):
#     c0, c1, c2, c3 = no_beacon_areas[i]
#     negative_lines[c0[0] - c0[1]] = negative_lines.get(c0[0] - c0[1], []) + [i]
#     negative_lines[c2[0] - c2[1]] = negative_lines.get(c2[0] - c2[1], []) + [i]
#     positive_lines[c0[0] + c0[1]] = positive_lines.get(c0[0] + c0[1], []) + [i]
#     positive_lines[c2[0] + c2[1]] = positive_lines.get(c2[0] + c2[1], []) + [i]

# negatives = sorted(set(negative_lines.keys()))
# positives = sorted(set(positive_lines.keys()))

negatives = []
positives = []
for corners in no_beacon_areas:
    negatives.append(corners[0][0] - corners[0][1])
    negatives.append(corners[2][0] - corners[2][1])
    positives.append(corners[0][0] + corners[0][1])
    positives.append(corners[2][0] + corners[2][1])

negatives.sort()
positives.sort()

for i in range(len(negatives)-1):
    diff = negatives[i+1] - negatives[i]
    if 0 < diff < 10:
        negatives = [negatives[i], negatives[i+1]]
        break

for i in range(len(positives)-1):
    diff = positives[i+1] - positives[i]
    if 0 < diff < 10:
        positives = [positives[i], positives[i+1]]
        break

n = sum(negatives)//2
p = sum(positives)//2

x = (p+n)/2
y = (p-n)/2

print(width*x + y)
        

ax = plt.subplot()

for corners in no_beacon_areas:
    ax.fill([p[0] for p in corners] + [corners[0][0]], [p[1] for p in corners] + [corners[0][1]])

ax.set_xlim(0, width)
ax.set_ylim(0, width)

plt.show()