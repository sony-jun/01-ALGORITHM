# https://www.acmicpc.net/problem/8958
from os import O_EXCL
import sys

sys.stdin = open("3_OX퀴즈.txt")


ox = int(input())

for i in range(ox):
    a = list(input())
    score = 0 # 연속 정답일 때 점수
    sum = 0 # O의 총 개수
    for j in a:
        if j == 'O':
            score += 1 # O의 연속된 개수 세기
        else:
            score = 0 # X일 때 초기화
    sum = sum + score
    print(sum)