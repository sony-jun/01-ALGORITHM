n,m = 8,8
c = 0
board = [list(input()) for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0 and board[i][j] == 'F':
            c += 1
print(c)