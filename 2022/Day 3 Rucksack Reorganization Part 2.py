# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 12:47:38 2022

Description
-----------
Advent of Code
Day 3: Rucksack Reorganizations Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"
priority = {(alphabet + alphabet.upper())[i]: i+1 for i in range(52)}

f = open("Day 3 Rucksack Reorganization.txt", "r")

lines = f.read().split("\n")[:-1]

total = 0
for i in range(0, len(lines), 3):
    badge_set = set(lines[i])
    badge_set.intersection_update(set(lines[i+1]))
    badge_set.intersection_update(set(lines[i+2]))
    
    for badge in badge_set:
        total += priority[badge]
        
print(total)
    