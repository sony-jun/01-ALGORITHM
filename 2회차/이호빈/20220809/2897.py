r, c = map(int, input().split())

board = []

#사방탐색 자기자신, 우, 하, 우하 (0,0) 시작
dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

# 2차원 배열 만듬
for _ in range(r):
    board.append(list(input()))

#행과 열이 (3,3)까지이니까 인덱스 초과하니까
for x in range(r-1):
    for y in range(c-1):
        result = 0
        #사방탐색 하면서
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            #만약에 빌딩을 만나면 -1 해준다.
            if board[nx][ny] == "#":
                result = -1
                break
            #만약에 x를 만나면 결과에 +=1을 더해준다. 
            elif board[nx][ny] == "X":
                result += 1

    

            
