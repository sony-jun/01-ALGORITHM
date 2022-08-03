n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    s=0
    i, j, x, y = map(int,input().split())
    for idx1 in range(i-1,x):
        s += sum(matrix[idx1][j-1:y])
    print(s)