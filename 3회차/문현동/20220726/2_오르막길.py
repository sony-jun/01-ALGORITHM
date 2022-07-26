import sys

sys.stdin = open("2_오르막길.txt")

n = int(input()) # 6
load = list(map(int, input().split())) # 10 8 8 6 4 3

section = []
uphill = []
elevation_dif = []

for i in range(1, n): # 1 ~ 5
    if load[i] > load[i - 1]:
        section.append(load[i - 1])
        section.append(load[i])
    else:
        if section:
            uphill.append(section)
            section = []
        else:
            pass

if section:
    uphill.append(section)

if uphill:
    for j in uphill:
        elevation_dif.append(max(j) - min(j))
    print(max(elevation_dif))
else:
    print(0)