import sys

sys.stdin = open("_13567.txt", "r")

dx = [1, 0, -1, 0] #동 남 서 북
dy = [0, -1, 0, 1]
nx = 0
ny = 0
dir = 0

M, N = map(int, input().split())

valid = True
for _ in range(N):
    A, B = input().split()
   
    if A == "TURN":
        if B == "0":
            if dir == 0:
                dir = 3
            else:
                dir -= 1
        elif B == "1":
            dir = (dir+1) % 4

    elif A == "MOVE":
        nx += dx[dir] * int(B)
        ny += dy[dir] * int(B)
        if not(0 <= nx <= M and 0 <= ny <= M):
            valid = False
            break

if valid:
    print(nx, ny)
else:
    print(-1)
