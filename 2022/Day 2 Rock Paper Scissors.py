# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Wed Dec 14 12:41:40 2022

Description
-----------
Advent of Code
Day 2: Rock Paper Scissors
"""

import numpy as np
import matplotlib.pyplot as plt

opponent = {'A': 0, 'B': 1, 'C': 2}
player = {'X': 0, 'Y': 1, 'Z': 2}

round_outcome = np.array([[3, 6, 0],
                          [0, 3, 6],
                          [6, 0, 3]])

f = open("Day 2 Rock Paper Scissors.txt", "r")

total_score = 0
for line in f:
    if line == "\n":
        continue
    
    opponent_choice = opponent[line[0]]
    player_choice = player[line[2]]
    
    shape = player_choice + 1
    outcome = round_outcome[opponent_choice, player_choice]
    total_score += (shape + outcome)
    
print(total_score)