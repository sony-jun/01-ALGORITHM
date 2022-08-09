n = int(input())

matrix = [input() for _ in range(n)]
example = [input() for _ in range(n)]
ans = [[0] * n for _ in range(n)] 

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for row in range(n):
    for col in range(n):
        if matrix[row][col] == '*':
            for i in range(8):
                x = row + dr[i]
                y = col + dc[i]
                if 0 <= x < n and 0 <= y < n:
                    ans[x][y] += 1

for row_1 in range(n):
    for col_1 in range(n):
        if example[row_1][col_1] == '.':
            ans[row_1][col_1] = '.'

for row_2 in range(n):
    for col_2 in range(n):
        if example[row_2][col_2] == 'x' and matrix[row_2][col_2] == '*':
            for row_3 in range(n):
                for col_3 in range(n):
                    if matrix[row_3][col_3] == '*':
                        ans[row_3][col_3] = '*'
            
for i in ans:
    for j in range(n):
        print(i[j],end='')
    print()