n = int(input())
mat = [input() for _ in range(n)]
click = [input() for _ in range(n)]
a = [['.' for _ in range(n)] for _ in range(n)]
game = False

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if click[i][j] == 'x':
            if mat[i][j] == "*":
                game = True
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    if mat[x][y] == '*':
                        cnt += 1
            a[i][j] = str(cnt)
if game:
    for row in range(n):
        for col in range(n):
            if mat[row][col] == '*':
                a[row][col] = '*'
for i in range(n):
    print(''.join(a[i]))