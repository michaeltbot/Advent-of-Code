import re

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

decryption_key = 811589153

with open("Day 20 Grove Positioning System.txt", "r") as f:
    file = [int(x) for x in re.split(r'\n+', f.read()) if x != '']

N = len(file)
original = [Node(x*decryption_key) for x in file]
for i in range(N):
    original[i].prev = original[(i-1) % N]
    original[i].next = original[(i+1) % N]
    if original[i].value == 0:
        zero = original[i]

print(zero.value)

for n in range(10):
    print(n)
    for i in range(N):
        jump = original[i].value % (N-1)
        current = original[i].prev

        original[i].prev.next = original[i].next
        original[i].next.prev = original[i].prev

        for j in range(jump):
            current = current.next

        current.next.prev = original[i]
        original[i].next = current.next
        original[i].prev = current
        current.next = original[i]

total = 0
jump = 1000 % N
current = zero
for n in range(3):
    for j in range(jump):
        curent = current.next
    total += current.value

print(total)