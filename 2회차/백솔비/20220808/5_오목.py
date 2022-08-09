import sys
sys.stdin = open("5_오목.txt")

# 우 하 우하 우상 (제일 왼쪽 돌을 골라야하므로)
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

black = 1
white = 2
N = 19
board = [list(map(int, input().split())) for _ in range(N)]
flag = 0

for x in range(N):
    for y in range(N):
        if board[x][y] == black or board[x][y] == white:
            for d in range(4):
                stone = 1
                nx = x + dx[d]
                ny = y + dy[d]

                while True:
                    if not(0<= nx < N and 0 <= ny < N):
                        break
                    # 다른색 돌이면 탈출
                    if board[x][y] != board[nx][ny]:
                        break

                    stone += 1

                    nx = nx + dx[d]
                    ny = ny + dy[d]
                
                if stone == 5:
                    #이전 좌표
                    prev_x = x - dx[d]
                    prev_y = y - dy[d]

                    #육목 체크
                    if not(0 <= prev_x < N and 0 <= prev_y < N) or board[x][y] != board[prev_x][prev_y]:
                        print(board[x][y])
                        print(x+1, y+1)
                        flag = board[x][y]
                        
if not flag:
    print(flag)

