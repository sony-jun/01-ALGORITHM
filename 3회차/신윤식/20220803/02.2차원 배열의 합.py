# https://www.acmicpc.net/problem/2167

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int,input().split())

    total = 0

    for row in range(N):
        for column in range(M):
            if row >= i-1 and row <= x-1 and column >= j-1 and column <= y-1:
                total += matrix[row][column]
    
    print(total)