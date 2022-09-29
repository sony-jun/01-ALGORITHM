# https://www.acmicpc.net/problem/2167

import sys
sys.stdin = open('2.txt', 'r')
from pprint import pprint

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
k = int(input())

for b in range(k):
    i, j, x, y = map(int,input().split())
    sum_ = 0
    for c in range(i-1,x):
        for d in range(j-1,y):
            sum_ += a[c][d]
    print(sum_)

#? 동적 계획법
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# memo = [[0] * (m+1) for _ in range(n+1)]

 
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
#         print(  memo[i][j-1])
 
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])