import sys
input = sys.stdin.readline

N, M = map(int, input().split())

castle = [list(input().rstrip()) for i in range(N)]
cnt1 = 0
cnt2 = 0

for i in range(N):
    if 'X' not in castle[i]:
        cnt1 += 1

for j in range(M):
    if "X" not in [castle[i][j] for i in range(N)]:
        cnt2 += 1

print(max(cnt1, cnt2))