n = int(input())
lst = [input().split() for _ in range(n)]
count_row = 0
count_column = 0
for i in range(n):
    list_col =[]
    list_row = ''.join(lst[i])
    if '..' in list_row:
        count_row += 1
    for j in range(n):
        list_col.append(lst[j][i])
    list_col = ''.join(list_col)
    if '..' in list_col:
        count_column += 1
print(count_row, count_column)