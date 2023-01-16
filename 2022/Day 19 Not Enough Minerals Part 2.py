import numpy as np
import re

def max_geodes(blueprint):
    max_spend = np.max(blueprint, axis=0)
    max_spend[3] = 100
    robots_resources = {(1, 0, 0, 0): {(0, 0, 0, 0)}}
    for n in range(32):
        max_resources = max_spend*(32-n)
        new_robots_resources = dict()
        for robots_key, resources_set in robots_resources.items():
            robots = np.array(robots_key)
            for resources in resources_set:
                resources = np.array(resources)
                new_resources = tuple(np.minimum(max_resources, resources + robots))
                try:
                    new_robots_resources[robots_key].add(new_resources)
                except KeyError:
                    new_robots_resources[robots_key] = {new_resources}

                for i in range(4):
                    if robots[i] < max_spend[i] and all(resources >= blueprint[i]):
                        new_robot = np.zeros(4)
                        new_robot[i] = 1
                        new_robots_key = tuple(robots + new_robot)
                        new_resources = tuple(np.minimum(max_resources, resources + robots - blueprint[i]))

                        try:
                            new_robots_resources[new_robots_key].add(new_resources)
                        except KeyError:
                           new_robots_resources[new_robots_key] = {new_resources}

        for resources_set in new_robots_resources.values():
            resources_list = list(resources_set)
            for r1 in resources_list:
                for r2 in resources_set:
                    if all(r1[i] <= r2[i] for i in range(4)) and r1 != r2:
                        resources_set.remove(r1)
                        break

        robots_resources = new_robots_resources
        
    return max(resources[3] for resources_set in robots_resources.values() for resources in resources_set)


pattern = r"Blueprint ([0-9]+): " \
    r"Each ore robot costs ([0-9]+) ore. " \
    r"Each clay robot costs ([0-9]+) ore. " \
    r"Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. " \
    r"Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.\n*"

total = 1
count = 0
for line in open("Day 19 Not Enough Minerals.txt", "r"):
    if count == 3:
        break

    m = re.match(pattern, line)
    blueprint_ID = int(m.group(1))
    costs = [int(m.group(i)) for i in range(2, 8)]
    blueprint = np.array([[costs[0], 0, 0, 0], [costs[1], 0, 0, 0], [costs[2], costs[3], 0, 0], [costs[4], 0, costs[5], 0]])
    
    geodes = max_geodes(blueprint)
    print(blueprint_ID, geodes)

    total *= geodes
    count += 1

print(total)