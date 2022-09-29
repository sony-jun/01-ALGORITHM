import sys
# import numpy as np
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for case in range(K):
    i, j, x, y = map(int, input().split())
    ans = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            ans += matrix[a][b]
    print(ans)
    # numpy 이용해서 풀어보기
    # n = np.array(matrix)
    # print(sum(sum(n[i-1:x, j-1:y])))