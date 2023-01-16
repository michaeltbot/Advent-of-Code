# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Sat Dec 17 12:18:24 2022

Description
-----------
Advent of Code
Day 13: Distress Signal
"""

import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, node):
        self.children.append(node)
        node.parent = self

def string_to_tree(s):
    root = Node([])
    current_node = root
    i = 1
    while i < len(s) - 1:
        if s[i] == "[":
            child_node = Node([])
            current_node.add_child(child_node)
            current_node = child_node
            i += 1
        elif s[i] == "]":
            current_node = current_node.parent
            i += 1
        elif s[i] == ",":
            i += 1
        else:
            num_str = ""
            while not (s[i] == "," or s[i] == "]"):
                num_str += s[i]
                i += 1
            num = int(num_str)
            current_node.add_child(Node(num))
    return root

def tree_to_list(root):
    l = []
    for node in root.children:
        if node.data == []:
            l.append(tree_to_list(node))
        else:
            l.append(node.data)
    return l

def string_to_list(s):
    root = string_to_tree(s)
    return tree_to_list(root)

def compare_packets(p1, p2):
    if type(p1) == type(p2) == list:
        i = 0
        while i < len(p1) and i < len(p2):
            result = compare_packets(p1[i], p2[i])
            if result != 0:
                return result
            i += 1
        return compare_packets(len(p1), len(p2))
    elif type(p1) == type(p2) == int:
        if p1 < p2:
            return 1
        elif p1 > p2:
            return -1
        else:
            return 0
    elif type(p1) == int and type(p2) == list:
        return compare_packets([p1], p2)
    elif type(p1) == list and type(p2) == int:
        return compare_packets(p1, [p2])

packets = []
with open("Day 13 Distress Signal.txt", "r") as f:
    for line in f:
        if line == "\n":
            continue
        line = line.rstrip("\n")
        
        packets.append(string_to_list(line))

total = 0
for i in range(0, len(packets), 2):
    if compare_packets(packets[i], packets[i+1]) == 1:
        total += i//2 + 1

print(total)
        
