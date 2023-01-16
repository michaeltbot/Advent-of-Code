# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 17:27:01 2022

Description
-----------
Advent of Code
Day 6: Tuning Trouble Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

with open("Day 6 Tuning Trouble.txt", "r") as f:
    data = f.read().rstrip("\n")

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        break

print(i+14)