import sys

sys.stdin = open('성지키기_input.txt')

# 세로 : N 가로 : M

# M, N = map(int, input().split())

# castle = [input() for i in range(M)]
# cnt = 0

# for i in range(M):
#     for j in range(N):
#         if castle[i][j] == 'X':
#             cnt += 1
#             break
# print(M-cnt)


N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]
cnt = 0
cnt2 = 0

for i in range(N):
    if 'X' not in castle[i]:
        cnt += 1
for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        cnt2 += 1

print(max(cnt, cnt2))