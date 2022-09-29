import sys
sys.stdin = open('test.txt', 'r')

move = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}

number = ['8', '7', '6', '5', '4', '3', '2', '1']
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
board = []
for i in range(8):
    line = []
    for j in range(8):
        line.append(0)
    board.append(line)

kp, sp, times = list(map(str, input().split()))
kj, ki = kp
sj, si = sp
kj = alpha.index(kj)
ki = number.index(ki)
sj = alpha.index(sj)
si = number.index(si)
for _ in range(int(times)):
    board[si][sj] = 1
    com = input()
    di, dj = move[com]
    nki = ki + di
    nkj = kj + dj
    if nki in range(8) and nkj in range(8):
        if board[nki][nkj] == 1:
            nsi = si + di
            nsj = sj + dj
            if nsi in range(8) and nsj in range(8):
                board[si][sj] = 0
                ki, kj, si, sj = nki, nkj, nsi, nsj
        else:
            ki, kj = nki, nkj

king = alpha[kj] + number[ki]
stone = alpha[sj] + number[si]
print(king)
print(stone)