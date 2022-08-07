# https://www.acmicpc.net/problem/9455

# m행 n열 그리드  일부 박스들 움직일 수 없을 때 까지 아래로 움직이면 쌓임
# 박스 움직인 거리 = 쌓이기 전까지 박스들의 이동 칸 수
# 1줄: 테스트 케이스 / 2줄:m행,n열 / 3줄~m줄:그리드 상태 1박스 0빈칸 사이는 공백있음!!
# 케이스별로 총 이동거리 출력

from pprint import pprint
import sys
sys.stdin = open('77_박스.txt')

# t = int(input())
# for test_case in range(1, t+1):
m, n = map(int, input().split())
greed = [list(map(int, input().split())) for _ in range(m)]
# pprint(greed)
cnt = 0
for i in (range(n)):
    for j in reversed(range(m)):
        # print(j, i)
        if greed[j][i] == 1:
                if greed[j-1][i] == 1:
                    greed[j][i] = 1
                    greed[j-1][i] = 0
                    cnt += 1
                    if j+1 != m-1 and greed[j+1][i] != 1:
                        greed[j+1][i] = 1
                        greed[j][i] = 0
                        cnt += 1 

