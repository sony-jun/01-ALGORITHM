n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(input())

# rc = row_count / cc = column count
rc, cc = 0, 0

for i in range(n):  # 가로줄을 돌림.
    if 'X' not in matrix[i] :
        rc += 1
        
for j in range(m):  # 세로줄을 돌림.
    if "X" not in [matrix[i][j] for i in range(n)]:        
        cc += 1

print(max(rc, cc))