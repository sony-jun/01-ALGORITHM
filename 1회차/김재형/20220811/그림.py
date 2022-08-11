import sys
sys.stdin = open('그림_input.txt')
from pprint import pprint

n, m = map(int, input().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# [[1, 1, 0, 1, 1],
#  [0, 1, 1, 0, 0],
#  [0, 0, 0, 0, 0],
#  [1, 0, 1, 1, 1],
#  [0, 0, 1, 1, 1],
#  [0, 0, 1, 1, 1]]

paint = []
for _ in range(n):
    a = list(map(int, input().split()))
    paint.append(a)

for x in range(n):
    for y in range(m):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                x = nx
                y = ny
                if 