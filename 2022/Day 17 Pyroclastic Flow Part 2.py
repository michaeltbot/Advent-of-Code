import numpy as np

rocks_str = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""

rock_strs = rocks_str.split("\n\n")

rock_types = []
for s in rock_strs:
    rock = []
    rows = s.split("\n")
    for i in range(len(rows)):
        row = rows[-i-1]
        for j in range(len(row)):
            if row[j] == "#":
                rock.append((j, i))
    rock_types.append(rock)

rock_heights = [max(y for _, y in rock) for rock in rock_types]

def collides(chamber, x, y, rock_type):
    return any(chamber[x + s, y + t] == 1 for s, t in rock_types[rock_type])

with open("Day 17 Pyroclastic Flow.txt", "r") as f:
    jet_pattern = f.read().rstrip("\n")

def next_rock(chamber, height, jet, rock_type):
    x = 3
    y = height + 4
    falling = True
    while falling:
        if jet_pattern[jet] == "<":
            direction = -1
        elif jet_pattern[jet] == ">":
            direction = 1
        
        if not collides(chamber, x + direction, y, rock_type):
            x += direction

        if collides(chamber, x, y - 1, rock_type):
            for s, t in rock_types[rock_type]:
                chamber[x + s, y + t] = 1
            height = max(height, y + rock_heights[rock_type])
            falling = False
        else:
            y -= 1

        jet += 1
        jet %= len(jet_pattern)
    return height, jet

N = 10**12
start = 1000
chamber = np.zeros((9, 13*2*start//5))
chamber[:, 0] = np.ones(9)
chamber[0, :] = np.ones(chamber.shape[1])
chamber[8, :] = np.ones(chamber.shape[1])

jet = 0
height = 0
for n in range(start):
    height, jet = next_rock(chamber, height, jet, n % 5)
start_height = height

periodic_jets = [jet]
periodic_heights = [height]
height, jet = next_rock(chamber, height, jet, start % 5)

n = start + 1
while jet != periodic_jets[0] or len(periodic_jets) % 5 != 0:
    periodic_jets.append(jet)
    periodic_heights.append(height)
    height, jet = next_rock(chamber, height, jet, n % 5)
    n += 1

periodic_height_differences = [periodic_heights[i+1] - periodic_heights[i] for i in range(len(periodic_heights) - 1)]
periodic_height_differences.append(height - periodic_heights[-1])

next_height = height + periodic_height_differences[0]
height, jet = next_rock(chamber, height, jet, n % 5)
print(height == next_height) # Test

# Print visual represntation
# for y in range(height, 0, -1):
#     s = "".join("#" if chamber[x][y] == 1 else "." for x in range(1, 8))
#     print("|" + s + "|")
# print("+-------+")

period = len(periodic_height_differences)
period_height_difference = sum(periodic_height_differences)

rock_number = N - start
height = start_height + (rock_number//period)*period_height_difference
for n in range(rock_number % period):
    height += periodic_height_differences[n]

print(height)