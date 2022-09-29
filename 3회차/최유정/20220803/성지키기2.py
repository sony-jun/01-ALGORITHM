row, col = map(int, input().split()) #3 5
castle = [list(input()) for r in range(row)]

col_cnt, row_cnt = 0, 0
 
for i in range(row):
    if "X" not in castle[i]:
        row_cnt += 1
 
for j in range(col):
    if "X" not in [castle[i][j] for i in range(row)]:
        col_cnt += 1

print(max(row_cnt,col_cnt))