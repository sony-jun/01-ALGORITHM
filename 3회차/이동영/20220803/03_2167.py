import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    count = 0

    for a in range(i-1, x):
        for b in range(j-1,y):
            count += matrix[a][b]

    print(count)