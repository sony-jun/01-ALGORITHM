import sys
from pprint import pprint
sys.stdin = open("2_몬스터트럭.txt", 'r')

R, C = map(int, sys.stdin.readline().split())

X_cnt = 0
dot_cnt = 0
space = []
matrix = []
dx = [0, 0, 1, 1]
dy = [0, 1, 1, 0]

for _ in range(R):
    matrix.append(sys.stdin.readline().rstrip())

for _ in range(5):
    space.append(0)

for x in range(R):
    for y in range(C):
        if matrix[x][y] != '#':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < R and ny < C:
                    if matrix[nx][ny] == '.':
                        dot_cnt += 1
                    elif matrix[nx][ny] == 'X':
                        X_cnt += 1
                    else:
                        dot_cnt = 0
                        X_cnt = 0
                        break
                else:
                    dot_cnt = 0
                    X_cnt = 0
                    break
            if dot_cnt + X_cnt == 4:
                space[dot_cnt] += 1
                dot_cnt = 0
                X_cnt = 0
for i in space[::-1]:
    print(i)