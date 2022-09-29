from pprint import pprint



n, m = map(int,input().split())


matrix=[list(input()) for __ in range(n)]



hx = 0
rx = 0


for i in matrix:
    if 'X' in i :
        hx += 1


for i in range(m):
    for j in range(n):
        if matrix[j][i] == 'X':
            rx += 1
            break

result =max(n-hx,m-rx)
print(result)