import sys

sys.stdin = open("input.txt", "r")

# 우선 100 100 배열 도화지를 만들자
coordi = [[0]*101 for _ in range(101)]

# 4번 반복하는 동안 도화지레 색칠
for _ in range(4):

    i, j, x, y = map(int, input().split())

    for a in range(i,x):
        for b in range(j,y):
            coordi[a][b] = 1
width = 0
for a in range(len(coordi)):
    for b in range(len(coordi)):
        if coordi[a][b] > 0:
            width += 1

print(width)