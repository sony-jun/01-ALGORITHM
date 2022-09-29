import sys
sys.stdin = open("20220811/13576_로봇.txt")

M, n = map(int, input().split()) # 정사각형 길이, 움직이는 횟수
rx, ry = 0, 0                    # 로봇 x, y 좌표

for i in range(n):               # n번 움직임
    cmd, d = input().split()     # 명령, 숫자
    x, y = 0, 0

    if cmd == 'TURN':
        x, y = 0, 0

    if cmd == 'MOVE':
        x, y = 0, 0
        if 0 <= rx + x < 8 and 0 <= ry + y < 8:
            rx += x
            ry += y
        else:
            print(-1)
            break

print(x, y)