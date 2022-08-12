# 로봇
import sys
sys.stdin = open('13567.txt')

M, n = map(int, input().split())
x = 0
y = 0
a = 0
b = 0
for _ in range(n):
    order = input().split()
    if order[0] == 'TURN':
        if order[1] == '0':
            b += 1
            if b > 3:
                b = 0
        else:
            b -= 1
            if b < 0:
                b = 3
    else:
        a = int(order[1])
        direction = [(0, a), (a, 0), (0, -a), (-a, 0)]
        dir = direction[b]
        x += dir[0]
        y += dir[1]
        if x > M or x < 0 or y > M or y < 0:
            print(-1)
            break
if 0 <= x <= M and 0 <= y <= M:
    print(y, x)