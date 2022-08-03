n,m = map(int,input().split())

matrix = [list(map(str,input())) for i in range(n)]

row_index = []
column_index = []

for j in range(n):
    if "X" not in matrix[j]:
        row_index.append(j)
new_matrix = []
for i in zip(*matrix):
    new_matrix.append(i)

for l in range(m):
    if "X" not in new_matrix[l]:
        column_index.append(l)

print(max(len(column_index),len(new_matrix)))