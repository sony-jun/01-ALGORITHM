# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("2953.txt")

cook_idx = 0 # 우승자의 번호
score = 0 # 점수
for i in range(5):
    a, b, c, d = map(int, input().split())
    sum_ = a + b + c + d
    if score < sum_:
        score = sum_
        cook_idx = i + 1
print(cook_idx, score)

