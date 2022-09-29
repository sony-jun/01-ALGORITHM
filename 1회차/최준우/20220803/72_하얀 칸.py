# https://www.acmicpc.net/problem/1100

chess_board = [list(map(str, input())) for _ in range(8)]
result = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0 and chess_board[i][j] != '.':
            result += 1
print(result)