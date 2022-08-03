board = []
for _ in range(8):
    board.append(input())

count = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'F':
            # 아래 조건이 더 깔끔하다.
            # if (x + y) % 2 == 0 and chess[x][y] == 'F':
            # 짝수 줄에 짝수번이 하양
            if not i % 2 and not j % 2:
                count += 1
            # 홀수 줄에 홀수번이 하양
            elif i % 2 and j % 2:
                count += 1

print(count)