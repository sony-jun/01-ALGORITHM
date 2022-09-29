# 2953
"""
"""
import sys
sys.stdin = open("요리사.txt")

# 각 참가자의 점수를 저장할 딕셔너리
score = {}
for idx in range(1, 6):
    score[idx] = sum(map(int, input().split()))

for key in score:
    if score[key] == max(score.values()):
        print(key, score[key])
        break