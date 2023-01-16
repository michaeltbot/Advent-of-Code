# -*- coding: utf-8 -*-
"""
Author:    Michael Bottomley
Created: Thu Dec 15 18:21:10 2022

Description
-----------
Advent of Code
Day 7: No Space Left On Device Part 2
"""

import numpy as np
import matplotlib.pyplot as plt

class Directory:
    def __init__(self, name):
        self.name = name
        self.directories = dict()
        self.files = []
        self.size = 0
    
    def add_directory(self, directory):
        self.directories[directory.name] = directory
        directory.parent = self
    
    def add_file(self, file):
        self.files.append(file)
        
    def get_directory(self, name):
        return self.directories[name]
    
    def get_parent(self):
        return self.parent
    
    def calculate_size(self):
        self.size = sum(file.size for file in self.files)
        self.size += sum(d.calculate_size() for d in self.directories.values())
        return self.size
    
    def get_all_directories(self):
        all_dir = []
        for d in self.directories.values():
            all_dir.append(d)
            all_dir += d.get_all_directories()
        return all_dir
        
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
class Tree:
    def __init__(self):
        self.root = Directory("/")
        self.current_dir = self.root
    
    def add_directory(self, name):
        self.current_dir.add_directory(Directory(name))
    
    def add_file(self, name, size):
        self.current_dir.add_file(File(name, size))
        
    def calculate_sizes(self):
        self.root.calculate_size()
    
    def open_directory(self, name):
        self.current_dir = self.current_dir.get_directory(name)
        
    def open_parent(self):
        self.current_dir = self.current_dir.get_parent()
        
    def open_root(self):
        self.current_dir = self.root
        
    def ls(self):
        for d in self.current_dir.directories.values():
            print("dir", d.name)
        for f in self.current_dir.files:
            print(f.size, f.name)
        
    def get_all_directories(self):
        return [(self.root.name, self.root.size)] + [(d.name, d.size) for d in self.root.get_all_directories()]
    
    def get_total_size(self):
        return self.root.size

tree = Tree()

f = open("Day 7 No Space Left On Device.txt", "r")

for line in f:
    if line == "\n":
        continue
    line = line.rstrip("\n")
    
    if line[0] == "$":
        if line[2:4] == "ls":
            continue
        
        name = line[5:]
        if name == "/":
            tree.open_root()
        elif name == "..":
            tree.open_parent()
        else:
            tree.open_directory(name)
    else:
        type_size, name = line.split(" ")
        if type_size == "dir":
            tree.add_directory(name)
        else:
            tree.add_file(name, int(type_size))

tree.calculate_sizes()
directories = tree.get_all_directories()

total_space = 70000000
needed_space = 30000000
free_space = total_space - tree.get_total_size()
delete_space = needed_space - free_space

smallest_size = min(size for name, size in directories if size >= delete_space)
print(smallest_size)