import sys
# import numpy as np
input = sys.stdin.readline

N = int(input())
numgame = [[], [], []]

for _ in range(N):
    a, b, c = map(int, input().split())
    numgame[0].append(a)
    numgame[1].append(b)
    numgame[2].append(c)

for i in range(N):
    score = 0
    for j in range(3):
        if numgame[j].count(numgame[j][i]) == 1:
            score += numgame[j][i]
    print(score)


#문제 잘못읽고 푼 코드
# numgame = [list(map(int, input().split())) for _ in range(N)]

# for i in range(N):
#     comparelist = np.delete(numgame, i, axis=0)
#     score = 0
#     for j in range(3):
#         if numgame[i][j] not in comparelist:
#             score += numgame[i][j]
#     print(score)
 