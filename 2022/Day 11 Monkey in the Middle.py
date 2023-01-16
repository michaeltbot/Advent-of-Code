# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Fri Dec 16 15:38:18 2022

Description
-----------
Advent of Code
Day 11: Monkey in the Middle
"""

import numpy as np
import matplotlib.pyplot as plt

def evaluate(operation, operand, x):
    if operation == "*":
        return x * operand
    elif operation == "+":
        return x + operand
    elif operation == "^":
        return x ** operand

held_items = dict()
operation = dict()
test_divisibility = dict()
throw_true = dict()
throw_false = dict()

with open("Day 11 Monkey in the Middle.txt", "r") as f:
    monkey_data = f.read().split("\n\n")

N = len(monkey_data)

# set up the data in useable format    
for n in range(N):
    lines = monkey_data[n].split("\n")
    
    starting_items = lines[1].lstrip("Starting items: ").split(", ")
    held_items[n] = [int(x) for x in starting_items]
    
    equation = lines[2].lstrip(" ").replace("Operation: ", "").split(" ")
    if equation[4] == "old":
        operation[n] = ("^", 2)
    else:
        operation[n] = (equation[3], int(equation[4]))
    
    test_divisibility[n] = int(lines[3].lstrip("Test: divisible by "))
    
    throw_true[n] = int(lines[4][-1])
    throw_false[n] = int(lines[5][-1])
    
items_inspected = {n: 0 for n in range(N)}

for r in range(20):
    for n in range(N):
        for worry in held_items[n]:
            worry = evaluate(operation[n][0], operation[n][1], worry)
            items_inspected[n] += 1
            worry //= 3
            if worry % test_divisibility[n] == 0:
                held_items[throw_true[n]].append(worry)
            else:
                held_items[throw_false[n]].append(worry)
        held_items[n] = []

inspection_numbers = list(items_inspected.values())
inspection_numbers.sort()
print(inspection_numbers[-1]*inspection_numbers[-2])