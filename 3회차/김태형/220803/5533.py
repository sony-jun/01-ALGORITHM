# 각 플레이어가 각각 쓴 수가 주어졌을 때, 3번 게임에서 얻은 총 점수를 구하는 프로그램을 작성하시오.

import sys

N = int(input())
score = []
for i in range(N):
    n = list(map(int,sys.stdin.readline().split()))
    score.append(n)

# print(score)