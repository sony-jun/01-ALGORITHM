n = 4
board = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

total = 0
for line in board:
    total += sum(line)
# print(sum(map(sum, matrix)))

print(total)
