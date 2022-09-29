import sys

sys.stdin = open('미로 탐색.txt')

N,M = map(int,input().split())

matrix = [list(input().split()) for _ in range(N)]

델타_y = [-1, 0, 0, 1]
델타_x = [0, -1, 1, 0]

T = 1
x=1
y=1
tmp_x = 0
tmp_y = 0
sum = 0
result = []

while():
    matrix[x][y]
    for d in range(4):
        cnt = 0
        탐색_x = x + 델타_x[d]
        탐색_y = y + 델타_y[d]
        if (탐색_x < 0  or 탐색_y < 0 
            or 탐색_x > N or 탐색_y> M or 
            (tmp_x == 탐색_x and tmp_y == 탐색_y)):
            continue
        if matrix[x][y] == matrix[탐색_x][탐색_y]:
       