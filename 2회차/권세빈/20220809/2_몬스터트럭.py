import sys
sys.stdin = open('2.txt','r')
from pprint import pprint

r,c = map(int,input().split())
p = [list(input()) for _ in range(r)]

car = [0]*5

for i in range(r-1):
    for j in range(c-1):
        t = []
        t.append(p[i][j])
        t.append(p[i][j+1])
        t.append(p[i+1][j+1])
        t.append(p[i+1][j])

        if '#' not in t:
            if t.count('X')
