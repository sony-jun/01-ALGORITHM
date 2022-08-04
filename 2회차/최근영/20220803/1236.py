n,m = map(int,input().split())

matrix = [list(map(str,input())) for _ in range(n)]

row_index = 0
column_index = 0

for j in range(n):
    for i in range(m):
        if "X" not in matrix[j]:
            row_index+=1
            if "X" not in matrix[j][i]:
                pass