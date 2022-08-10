import sys
input = sys.stdin.readline

R, C = map(int, input().split())

parking = [list(input().rstrip()) for _ in range(R)]
mtruck = [0, 0, 0, 0, 0]
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

for x in range(R-1):
    for y in range(C-1):
        cnt = 0
        available = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if parking[nx][ny] == '#':
                cnt = 0
                available = False
                break
            elif parking[nx][ny] == 'X':
                cnt += 1

        if available == True:
            mtruck[cnt] += 1

for i in range(5):
    print(mtruck[i])