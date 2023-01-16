# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 13:52:47 2022

Description
-----------
Advent of Code
Day 9: Rope Bridge
"""

import numpy as np
import matplotlib.pyplot as plt

def move(x, y, direction):
    if direction == "L":
        x -= 1
    elif direction == "R":
        x += 1
    elif direction == "U":
        y += 1
    elif direction == "D":
        y -= 1
    return x, y
        
def step(x_h, y_h, x_t, y_t, direction):
    x_h, y_h = move(x_h, y_h, direction)
    
    if -1 <= x_t - x_h <= 1 and -1 <= y_t - y_h <= 1:
        return x_h, y_h, x_t, y_t
    
    if x_t < x_h:
        x_t += 1
    elif x_t > x_h:
        x_t -= 1
        
    if y_t < y_h:
        y_t += 1
    elif y_t > y_h:
        y_t -= 1
    
    return x_h, y_h, x_t, y_t

visited = {(0, 0)}
x_h, y_h, x_t, y_t = 0, 0, 0, 0

for line in open("Day 9 Rope Bridge.txt", "r"):
    if line == "\n":
        break
    line = line.rstrip("\n")
    
    direction, steps = line.split(" ")
    for i in range(int(steps)):
        x_h, y_h, x_t, y_t = step(x_h, y_h, x_t, y_t, direction)
        print(x_h, y_h, x_t, y_t)
        visited.add((x_t, y_t))

print(len(visited))