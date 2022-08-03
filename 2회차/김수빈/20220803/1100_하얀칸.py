# chess = []

# for i in range(8):
#     chess_ = []
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             chess_.append('white')
#         else:
#             chess_.append('black')
#     chess.append(chess_)

# print(chess)

import sys
sys.stdin = open("1100_하얀칸.txt")

F = []
for _ in range(8):
    F.append(list(input()))

cnt = 0
for i in range(8):
    for j in range(8):
        if F[i][j] == 'F':
            if (i + j) % 2 == 0:
                cnt += 1

print(cnt)