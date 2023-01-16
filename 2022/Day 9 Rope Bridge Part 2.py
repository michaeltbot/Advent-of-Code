# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 13:52:47 2022

Description
-----------
Advent of Code
Day 9: Rope Bridge Part 2
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

def follow(x_h, y_h, x_t, y_t):
    if -1 <= x_t - x_h <= 1 and -1 <= y_t - y_h <= 1:
        return x_t, y_t
    
    if x_t < x_h:
        x_t += 1
    elif x_t > x_h:
        x_t -= 1
        
    if y_t < y_h:
        y_t += 1
    elif y_t > y_h:
        y_t -= 1
    
    return x_t, y_t

def step(x, y, direction):
    x[0], y[0] = move(x[0], y[0], direction)
    for i in range(1, len(x)):
        x[i], y[i] = follow(x[i-1], y[i-1], x[i], y[i])
    return x, y
    

visited = {(0, 0)}
x = [0 for i in range(10)]
y = [0 for i in range(10)]

for line in open("Day 9 Rope Bridge.txt", "r"):
    if line == "\n":
        break
    line = line.rstrip("\n")
    
    direction, steps = line.split(" ")
    for i in range(int(steps)):
        x, y = step(x, y, direction)
        visited.add((x[9], y[9]))

print(len(visited))