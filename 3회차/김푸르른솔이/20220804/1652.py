n = int(input()) 
matrix = []
for i in range(n):
    line = list(input())
    matrix.append(line)

cnt = 0
a = 0
b = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'X':
            cnt = 0
        else:
            cnt += 1
            if cnt == 2:
                a += 1
    cnt = 0

for i in range(n):
    for j in range(n):
        if matrix[j][i] == 'X':
            cnt = 0
        else:
            cnt += 1
            if cnt == 2:
                b += 1
    cnt = 0
print(a, b)

