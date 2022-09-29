# 방향벡터 : 좌상/좌/좌하//하/상//우상/우/우하 순서
dx = [-1, -1, -1, 0, 0 ,1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


N = int(input())
board = [input() for _ in range(N)] # 지뢰판
press = [input() for _ in range(N)] # 누른부분
answer = [['.' for _ in range(N)] for _ in range(N)] # 출력
gamerun = False # 진행 가능?
for i in range(N): 
    for j in range(N):
        if press[i][j] == "x": # 누른부분이 X인데
            if board[i][j] == "*": #지뢰가 있으면 
                gamerun = True # 더이상 진행불가
            cnt = 0
            for k in range(8):
                x = i + dx[k] # i주변 벡터 반환
                y = j + dy[k] # j주변 벡터 반환
                if 0<= x < N and 0 <= y < N: # 판때기 내에 있으면서
                    if board[x][y] == "*": # 지뢰가 범위내?
                        cnt += 1 # 지뢰수만큼 추가
            answer[i][j] = str(cnt) # join쓰게 문자열로 추가

if gamerun: #진행 불가능
    for row in range(N):
        for col in range(N):
            if board[row][col] == "*": # 지뢰있는칸
                answer[row][col] = "*" # *로 표시
for i in range(N):
    print(''.join(answer[i]))