# 19 줄 각 줄마다 N, 가로세로
# 가장 왼쪽에 있는 바둑알

BLACK = 1
WHITE = 2
N = 19

# 상 -> y -= 1
# 하 -> y +=1

# 우 하ㅣ 우상 우하
dy = [0,1,-1,1]
dx = [1,0,1,1]
board = []
answer = 0
# 오목판 상황 입력
for _ in range(N):
    # 하나의 행을 입력
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

    #이중 반복
    for y in range(N):
        for x in range(N):
            # 검은색돌이나 흰색돌일때만 델타 탐색을 수행ㄹ
            if board[y][x] == 1  or board[y][x] == 2:
                #델타 탐색
                for d in range(4):
                    # 방향이 바뀔 때마다 돌의 개수가 갱신
                    stone_count = 0
                    # 다음 좌표 탐색
                    ny = y + dx[d]
                    nx = x + dx[d]

                    while True:
                        # 인덱스 조건
                        if -1 < ny < N and -1 < nx < N:
                            break
                        # 같은색 (값) 돌인지 확인하는 조건
                        if not(board[y][x] == board[ny][nx]):
                            break

                        # 같은 값이고 범위를 벗어나지 않으면
                        stone_count += 1

                        # 같은 방향이고 다음 좌표를 탐색
                        ny = ny + dy[d]
                        nx = nx + dx[d]

                        # 돌의 개수가 5개라면
                        if stone_count == 5:
                            #이전 좌표
                            prev_y = y - dy[d]
                            prev_x = x - dx[d]
                            #육목인지 판단
                            # 조건 1. 이전 좌표가 범위를 벗어나면 오목
                            # if not(-1 < prev_y < N and -1 < prev_x < N):
                            
                            #조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                            # if board[y][x] != board[prev_y][prev_x]:

                            # 조건 1과 조건 2를 만족하면 오목이 완성
                            if not(-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:

                                # 현재 돌의 색 출력
                                print(board[x][y])
                                # 현재 돌의 좌표 출력
                                print(y + 1, x + 1)
                                # 실제 코딩테스트에서 사용이 불가능한 방법
                                # exit(0)
# 전체를 반복했는데 무승부

if answer == 0:


# 델타_y = [0,1,1,-1]
# 델타_x = [1,0,1,1]

# y = 2
# x = 2

# for d in range(4):
#     next_y = y + 델타_y[d]
#     next_x = x + 델타_x[d]
    
#     while True:
#         # 인덱스 범위 조건
#         if not(-1 < next_y < N and -1 < next_x < N):
#             break
#         # 돌 색깔 조건
#         if borad[next_y][next_x] != board[y][x]:
#             break

#         # 같은 색 돌 + 1
#         count +=1

#          다음 좌표 탐색