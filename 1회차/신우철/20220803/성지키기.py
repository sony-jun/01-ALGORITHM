# 1236
n, m = map(int,input().split())
matrix = []
a = 0
b = 0
for _ in range(n):
    matrix.append(input())
    
for i in range(n):
    if 'X' not in matrix[i]:
        a += 1
        
for j in range(m):
    if 'X' not in [matrix[i][j]for i in range(n)]:
        b += 1

print(max(a,b))
    
