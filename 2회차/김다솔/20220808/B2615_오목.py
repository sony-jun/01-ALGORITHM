import sys
sys.stdin = open('B2615.txt')

#우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]

black = 1
white = 0
N = 19

board = []

for _ in range(N):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

for y in range(N):
    for x in range(N):
        #델타탐색
        for d in range(4):
            #방향이 바뀔 때마다 돌의 개수가 갱신(0)
            stone_cnt = 0
            # 다음 좌표 탐색 
            ny = y + dy[d]
            nx = x + dx[d]
            
            while True:
                #인덱스 조건
                if not(-1 < ny < N and -1 < nx < N):
                    break
                
                #같은색(값) 돌인지 확인하는 조건 
                if not(board[y][x] == board[ny][nx]):
                    