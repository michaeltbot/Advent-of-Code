import re

with open("Day 20 Grove Positioning System.txt", "r") as f:
    file = [int(x) for x in re.split(r'\n+', f.read()) if x != '']

N = len(file)
l = [(i, file[i]) for i in range(N)]

for i in range(N):
    j = 0
    while l[j][0] != i:
        j += 1
    
    x = l.pop(j)
    l.insert((j + x[1]) % (N-1), x)

j = 0
while l[j][1] != 0:
    j += 1

print(l)
total = sum(l[(j + n)%N][1] for n in [1000, 2000, 3000])
print(total)