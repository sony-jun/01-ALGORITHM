N = int(input())

matrix = [input() for _ in range(N)]
count_row = 0
count_col = 0

if N == 1:
    print(0, 0)
    exit(0)

a = False  
for i in matrix:
    for j in range(N-1):
        if i[j] == '.':
            if i[j+1] == '.':
                a = True
            elif i[j+1] == 'X':
                if a == True:
                    count_row += 1
                    a = False
    else:
        if a == True:
            count_row += 1
            a = False

b = False
for k in range(N):
    for m in range(N-1):
        if matrix[m][k] == '.':
            if matrix[m+1][k] == '.':
                b = True
            elif matrix[m+1][k] == 'X':
                if b == True:
                    count_col += 1
                    b = False
    else:
        if b == True:
            count_col += 1
            b = False

print(count_row, count_col)