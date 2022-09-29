from sys import stdin as s
chessBoard = [list(s.readline()) for i in range(8)]
cnt = 0
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and chessBoard[i][j] == 'F':
            cnt += 1
print(cnt)