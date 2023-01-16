# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 12:47:38 2022

Description
-----------
Advent of Code
Day 3: Rucksack Reorganizations
"""

import numpy as np
import matplotlib.pyplot as plt

alphabet = "abcdefghijklmnopqrstuvwxyz"
priority = {(alphabet + alphabet.upper())[i]: i+1 for i in range(52)}

f = open("Day 3 Rucksack Reorganization.txt", "r")

total = 0
for line in f:
    if line == "\n":
        continue
    line = line.rstrip("\n")
    
    compartment_size = len(line)//2
    compartment1 = set(line[:compartment_size])
    compartment2 = set(line[compartment_size:])
    
    for item in compartment1.intersection(compartment2):
        total += priority[item]
        
print(total)