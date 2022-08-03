# https://www.acmicpc.net/problem/5533

N = int(input())
result = [0] * N
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

for j in range(3):
    round = [board[i][j] for i in range(N)]
    
    for i in range(N):
        if round.count(round[i]) == 1:
            result[i] += round[i]
for i in range(N):
    print(result[i])