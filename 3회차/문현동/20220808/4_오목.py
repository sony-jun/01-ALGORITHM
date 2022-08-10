import sys
from pprint import pprint
sys.stdin = open("4_오목.txt", 'r')

checker = []
for _ in range(19):
    checker.append([*map(int, sys.stdin.readline().split())])

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for x in range(19):
    if 1 or 2 in checker[x]:
        for y in range(19):
        