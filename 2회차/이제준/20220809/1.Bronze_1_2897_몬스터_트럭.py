
import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]

dr = [1, 1, 0]
dc = [0, 1, 1]

empty = '.'
car = 'X'
building = '#'

park = 0

for x in range(R):
    for y in range(C):
        
        cnt = 0
        # 차를 하나도 안 부수고 주차할 수 있는 공간
        if parking[x][y] == empty:

            # 델타 탐색하기
            for i in range(3):
                sr = dr[i] + x
                sc = dc[i] + y

                if 0 <= sr < R and 0 <= sc < C:
                    if parking[sr][sc] == empty:
                        cnt += 1
                        if cnt == 3:
                            park += 1


print(park)