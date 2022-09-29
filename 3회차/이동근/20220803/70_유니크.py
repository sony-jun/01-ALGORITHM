import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = [[], [], []]
for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    for i in range(3):
        board[i].append(line[i])

for i in range(N):
    ret = 0

    for j in range(3):
        if board[j].count(board[j][i]) == 1:
            ret += board[j][i]
    
    print(ret)
