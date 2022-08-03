# 백준 1236
# 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다
# 모든 행과 열에 한 명 이상의 경비원이 있으면 좋겠다
# 성의 크기와 경비원이 어디있는지 주어졌을 때
# 몇 명의 경비원을 최소로 추가해야 하는지

# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다
# 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다
# 성의 상태는 '.'은 빈칸, 'X'는 경비원이 있는 칸

# 첫째 줄에 추가해야 하는 경비원의 최솟값 출력

import sys
sys.stdin = open('성지키기.txt', 'r')

N, M = map(int, input().split())
castle = []

for _ in range(N):
    castle.append(input())

row, col = 0, 0

# castle[i] 인덱스에 'X'가 없다면 row에 1 더하기
for i in range(N):
    if 'X' not in castle[i]:
        row += 1

# castle[i][j]인덱스에 'X'가 없다면 col에 1 더하기
for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        col += 1
    
# 둘 중에 큰 수 출력
print(max(row, col))