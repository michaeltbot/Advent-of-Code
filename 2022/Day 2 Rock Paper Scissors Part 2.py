# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Wed Dec 14 12:41:40 2022

Description
-----------
Advent of Code
Day 2: Rock Paper Scissors Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

opponent = {'A': 0, 'B': 1, 'C': 2}
outcome = {'X': 0, 'Y': 1, 'Z': 2}

player_shape = np.array([[2, 0, 1],
                         [0, 1, 2],
                         [1, 2, 0]])

f = open("Day 2 Rock Paper Scissors.txt", "r")

total_score = 0
for line in f:
    if line == "\n":
        continue
    
    opponent_choice = opponent[line[0]]
    player_outcome = outcome[line[2]]
    
    total_score += (3*player_outcome + player_shape[opponent_choice, player_outcome] + 1)
    
print(total_score)