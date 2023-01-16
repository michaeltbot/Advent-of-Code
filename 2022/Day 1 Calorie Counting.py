# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Wed Dec 14 12:16:38 2022

Description
-----------
Advent of Code
Day 1: Calorie Counting
"""

import numpy as np
import matplotlib.pyplot as plt

with open("Day 1 Calorie Counting.txt", "r") as f:
    max_calorie = 0
    current_calorie = 0
    for line in f:
        if line == "\n":
            if current_calorie > max_calorie:
                max_calorie = current_calorie
            current_calorie = 0
            continue
        
        current_calorie += int(line.rstrip("\n"))

print(max_calorie)