# https://www.acmicpc.net/problem/2167
# pypy3
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for q in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for w in range(N):
        for e in range(M):
            if i - 1 <= w and w <= x - 1 and j - 1 <= e and e <= y - 1:
                result += board[w][e]
    print(result)