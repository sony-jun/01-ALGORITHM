import sys
from pprint import pprint

sys.stdin = open("1_직사각형.txt", 'r')

recs = []
plane = []

for n in range(100):
    plane.append([0] * 100)

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    for row in range(x1 - 1, x2 - 1):
        for column in range(y1 - 1, y2 - 1):
            plane[row][column] += 1
            
for row in plane:
    for column in range(len(row)):
        if row[column] > 1:
            row[column] = 1

print(sum(map(sum, plane)))