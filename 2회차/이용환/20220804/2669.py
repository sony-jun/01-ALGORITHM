import sys
input = sys.stdin.readline
matrix = [[0] * 100 for _ in range(100)]
for i in range(4):
    x, y, r, c = map(int, input().split())
    for j in range(x, r):
        for k in range(y, c):
            matrix[j][k] = 1
print(sum(map(sum, matrix)))