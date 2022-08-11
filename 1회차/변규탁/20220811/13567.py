import sys

sys.stdin = open("_13567.txt", "r")

dx = [1, 0, -1, 0] #동 남 서 북
dy = [0, 1, 0, -1]
x = 0
y = 0
dir = 0

M, N = map(int, input().split())

for _ in range(N):
    A, B = input().split()
    nx = x
    ny = y
    if A == "MOVE":
        if dir == 0:
            nx += dx[dir]*int(B)
        elif dir == 1:
            ny += dy[dir]*int(B)
        elif dir == 2:
            nx -= dx[dir]*int(B)
        elif dir == 3:
            ny -= dy[dir]*int(B)
    
    if A == "TURN":
        if B == "0":
            dir = (dir-1+4) % 4
        elif B == "1":
            dir = (dir+1) % 4

if 0 <= nx <= M and 0 <= ny <= M:
    print(nx, ny)
else:
    print(-1)
