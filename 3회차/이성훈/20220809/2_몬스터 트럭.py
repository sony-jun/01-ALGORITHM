# https://www.acmicpc.net/problem/2897
import sys

sys.stdin = open("2_몬스터 트럭.txt")

R, C = map(int, input().split())

print(R, C)

# 1. 델타값 정의(하,우하,우)
dy = [1, 1, 0]
dx = [0, 1, 1]

#2 . 이차원 리스트 순회
for y in range(R):
    for x in range(C):

        # 3.델타값을 이용해 하,우하,우 이동
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]

            # 4. 범위를 벗어나지 않으면 갱신
            if 0 <= nx < R and 0 <= nx < C:
                x = nx
                y = ny
                print(x,y)

