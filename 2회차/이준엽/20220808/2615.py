n = 19
dy = [0,1,-1,1]
dx = [1,0,1,1]

board = [list(map(int,input().split())) for i in range(n)]
answer = 0
for y in range(n):
    for x in range(n):
        if board[y][x] == 1 or board[y][x] == 2:
            for d in range(4):
                stone_count = 1
                ny = y+dy[d]
                nx = x+dx[d]

                while True:
                    if not (0<=ny<n and 0<=nx<n ):
                        break
                    if not (board[y][x] == board[ny][nx]):
                        break

                    stone_count +=1
                    ny = ny+dy[d]
                    nx = nx+dx[d]
                
                if stone_count == 5:
                    prevy = y - dy[d]
                    prevx = x - dx[d]
                    if not (0<=prevx<n and 0<=prevy<n) or board[y][x] != board[prevy][prevx]:
                        answer = board[y][x]
                        print(answer)
                        print(y+1,x+1)

if answer == 0:
    print(answer)