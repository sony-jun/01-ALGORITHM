# https://www.acmicpc.net/problem/4396
import sys

sys.stdin = open("1_직사각형 네개의 합집합의 면적 구하기.txt")

cnt = 0
blink_box = []

for i in range(100):
        blink_box.append([0] * 100)

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            blink_box[i][j] = 1

for i in range(100):
    for j in range(100):
        if blink_box[i][j] == 1:
            cnt += 1

print(cnt)
