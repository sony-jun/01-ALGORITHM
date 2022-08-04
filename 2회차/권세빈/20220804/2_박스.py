# https://www.acmicpc.net/problem/9455

import sys
sys.stdin = open('2.txt', 'r')
from pprint import pprint

T = int(input())
for t in range(T):
    m, n = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(5)]
    col_box = []

    for i in range(n):   
        col = [box[j][i] for j in range(m)]
        col_box.append(col)
        for k in range(4,-1,-1):
            print(col_box[i][k])

