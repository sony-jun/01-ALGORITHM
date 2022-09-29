# 2차원 배열의 합
# 문제 : 2차원 배열에 저장되어 있는 수의 합 구하기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

stack = [[0] * m] + [list(map(int, input().split())) for _ in range(n)]

for _ in range(int(input())):
    hap = 0
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1 - 1, y2):
            if x1 - 1 <= i <= x2 and y1 - 1 <= j <= y2:
                hap += stack[i][j]

    print(hap)
