# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 14:38:24 2022

Description
-----------
Advent of Code
Day 10: Cathode-Ray Tube Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

def update_screen(screen, pixel_position, X):
    if -1 <= pixel_position - X <= 1:
        screen += "#"
    else:
        screen += "."
    
    if pixel_position == 39:
        screen += "\n"
    
    return screen

screen = ""

pixel_position = 0
X = 1
adding = False
for line in open("Day 10 Cathode-Ray Tube.txt", "r"):
    if line == "\n":
        break
    line = line.rstrip("\n")
    
    screen = update_screen(screen, pixel_position, X)
    pixel_position += 1
    pixel_position %= 40
    
    if line == "noop":
        continue
    
    screen = update_screen(screen, pixel_position, X)
    pixel_position += 1
    pixel_position %= 40
    
    instruction, num = line.split(" ")
    X += int(num)
    
print(screen)