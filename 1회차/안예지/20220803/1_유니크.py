# 5533
"""
"""
from pprint import pprint

N = 5
score = [[100, 99, 98], 
         [100, 97, 92], 
         [63, 89, 63], 
         [99, 99, 99], 
         [89, 97, 98]]

# for _ in range(N):
#     score.append(list(map(int, input().split())))
# pprint(score)

# 행을 순회
round = 0
for row in score:
    score[round]