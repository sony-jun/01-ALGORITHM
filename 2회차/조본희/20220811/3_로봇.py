import sys
# from pprint import pprint
# sys.stdin = open('input.txt')
input = sys.stdin.readline

M, s = map(int, input().split())
grid = [[0] * M for _ in range(M)]
x = 0
y = 0
grid[x][y] = 1
dircnt = 0
err = True

for _ in range(s):
    inst, num = map(str, input().split())
    num = int(num)
    direction = [[num, 0], [0, num], [-num, 0], [0, -num]]

    if inst == 'TURN':
        if num == 0:
            dircnt += 1
            if dircnt > 3:
                dircnt -= 4
        elif num == 1:
            dircnt -= 1
            if dircnt < 0:
                dircnt += 4
                
    dx = direction[dircnt][0]
    dy = direction[dircnt][1]

    if inst == 'MOVE':
        try:
            grid[x + dx][y + dy] = 1
            grid[x][y] = 0
            x = x + dx
            y = y + dy
        except:
            print(-1)
            err = False
            break

if err:
    if 0 <= x < M and 0 <= y < M:
        print(x, y)
    else:
        print(-1)