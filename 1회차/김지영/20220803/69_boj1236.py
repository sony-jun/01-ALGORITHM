
n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]

temp = []
garo = 0
sero = 0
for i in range(n):
    if 'X' not in matrix[i]:
        garo += 1
for j in range(m):
    if 'X' not in [matrix[i][j] for i in range(n)]:
        sero += 1
print(garo if garo > sero else sero)