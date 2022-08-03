import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for tc in range(k):
    i, j, x, y = map(int, input().split())
    sum = 0

    # 1차원 인덱스는 i-1부터 x까지 세로로
    for a in range(i-1, x):
        # 2차원 인덱스는 j-1부터 y까지
        for b in range(j-1, y):
            sum += matrix[a][b]
    print(sum)