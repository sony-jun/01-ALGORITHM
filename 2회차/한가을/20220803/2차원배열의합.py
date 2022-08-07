# 백준 2167
# 2차원 배열이 주어졌을 때 (i, j) 위치부터
# (x, y) 위치까지에 저장되어 있는 수들의 합
# 배열의 (i, j) 위치는 i행 j열을 나타냄

# 첫째 줄에 배열의 크기 N, M이 주어진다
# 다음 N개의 줄에는 M개의 정수로 배열이 주어진다
# 그 다음 줄에는 합을 구할 부분의 개수 K가 주어진다
# 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다

# K개의 줄에 순서대로 배열의 합 출력

import sys
sys.stdin = open('2차원배열의합.txt', 'r')

N, M = map(int, input().split())
s = []
#* 0으로 초기화 된 N + 1행, M + 1열의 2차원 배열 만들기
r = [[0] * (M + 1) for _ in range(N + 1)]

#* N행 M열의 2차원 배열 만들기
for _ in range(1, N + 1):
    s.append(list(map(int, input().split())))

#* s의 (0, 0)부터 (i, j)까지의 합을 리스트 r에 저장
#* r의 (1, 1)부터 저장
for i in range(1, N + 1):
    for j in range(1, M + 1):
        r[i][j] = s[i - 1][j - 1] + r[i - 1][j] + r[i][j - 1] - r[i - 1][j - 1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(r[x][y] - r[x][j -1] - r[i - 1][y] + r[i - 1][j - 1])