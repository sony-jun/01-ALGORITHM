import sys
sys.stdin = open("4_오목.txt", 'r')

board = []
for _ in range(19):
    board.append([*map(int, sys.stdin.readline().split())])

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]
cnt = 0
winner = 0
for x in range(19):
    if 1 in board[x] or 2 in board[x]:
        for y in range(19):
            if board[x][y] != 0:
                cnt = 1
                for i in range(4): # 탐색할 위치로 좌표를 변경
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while -1 < nx < 19 and -1 < ny < 19:
                        if board[nx][ny] == board[x][y]:
                            cnt += 1
                            nx = nx + dx[i]
                            ny = ny + dy[i]
                        else:
                            break
                    if cnt != 5:
                        cnt = 1
                    elif cnt == 5:
                        if -1 < x - dx[i] < 19 and -1 < y - dy[i] < 19:
                            if board[x][y] != board[x - dx[i]][y - dy[i]]:
                                winner = board[x][y]
                                print(board[x][y])
                                print(x + 1, y + 1)
                                break
                            else:
                                cnt = 1
                        else:
                            winner = board[x][y]
                            print(board[x][y])
                            print(x + 1, y + 1)
                            break
if winner == 0:
    print(winner)