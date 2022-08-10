# import sys
# input = sys.stdin.readline
# # 인덱스 초과 방지 테두리 0 만들기 -> 인덱스도 각각 +1이므로 문제 바둑판 번호와 일치


# omok_matrix = [list(input().split()) for _ in range(19)]


# # case1. x일정 y증가  x:(1,19) y:(1,15)
# # case2. x증가 y증가  x:(1,15) y:(1,15)
# # case3. x증가 y감소  x:(1,15) y:(19,5)
# # case4. x증가 y일정  x:(1,15) y:(1,19)

# # [x,y]좌표 흰돌, 검은돌 각각 위치 리스트 생성
# white_lst = []
# black_lst = []
# for i in range(0,19):
#     for j in range(0,19):
        
#         if omok_matrix[i][j] == '1':
#             black_lst.append([i+1,j+1])
#         elif omok_matrix[i][j] == '2':
#             white_lst.append([i+1,j+1])

# # print(white_lst)
# # print(black_lst)


# def Omok(color_lst, color_num):
#     dx = [1,2,3,4,5]
#     dy = [1,2,3,4,5]
#     for coor in color_lst:
#         x = coor[0]
#         y = coor[1]
#         cnt1, cnt2 , cnt3, cnt4 = 0, 0, 0, 0
#         for i in range(5):
#             # print([x,y+dy[i]])
#             if [x,y+dy[i]] in color_lst:           # case 1
#                 cnt1 += 1
#                 if cnt1 == 5:
#                     color_lst.pop(color_lst.index([x,y+dy[i]]))

#             # print([x+dx[i],y+dy[i]])
#             if [x+dx[i],y+dy[i]] in color_lst:     # case 2
#                 cnt2 += 1
#                 if cnt2 == 5:
#                     color_lst.pop(color_lst.index([x+dx[i],y+dy[i]]))

#             # print([x+dx[i],y+dy[4-i]])
#             if [x+dx[i],y+dy[4-i]] in color_lst:   # case 3
#                 cnt3 += 1
#                 if cnt3 == 5:
#                     color_lst.pop(color_lst.index([x+dx[i],y+dy[4-i]]))

#             # print([x+dx[i],y])
#             if [x+dx[i],y] in color_lst:           # case 4
#                 cnt4 += 1
#                 if cnt4 == 5:
#                     color_lst.pop(color_lst.index([x+dx[i],y]))

#         # print(cnt1, cnt2, cnt3, cnt4)
#         if cnt1 == 4 or cnt2 == 4 or cnt3 == 4 or cnt4 == 4:
#             print(color_num)
#             print(*[x,y])
#             exit()
    

# coor_white = Omok(white_lst,2)
# coor_black = Omok(black_lst,1)
# print(0)



# ----------------------------------------------------------------------------------

# import sys
# from pprint import pprint

# # 우 하 우상 우하
# dy = [0, 1, -1, 1]
# dx = [1, 0, 1, 1]
# BLACK = 1
# WHITE = 2
# N = 19

# board = []

# # 오목판 상황 입력
# for _ in range(N):
#     # 하나의 행을 입력
#     temp_lst = list(map(int,input().split()))
#     board.append(temp_lst)

#     #이중 반복문
#     for y in range(N):
#         for x in range(N):
#             # 델타 탐색
#             for d in range(4):
#                 # 다음 좌표 탐색
#                 stone_count = 0
#                 ny = y + dy[d]
#                 nx = x + dx[d]

#                 while  True:
#                     # 인덱스 조건
#                     if not(-1 < ny < N and -1 < nx < N):
#                         break
#                 #같은색 돌인지 확인하는 조건
#                 if not(board[y][x] == board[ny][nx]):
#                     break

#                 # 같은 값이고 범위를 벗어나지 않으면
#                 stone_count += 1

#                 # 같은 방향 다음 좌표를 탐색
#                 ny = ny + dy[d]
#                 nx = nx + dx[d]

#             # 돌의 개수가 5개라면
#             if stone_count == 5:
#                 # 이전 좌표
#                 prev_y = y - dy[d]
#                 prev_x = x = dx[d]

#                 # 육목인지 판단
#                 # 조견1. 이전 좌표가 범위를 벗어나면 오목
#                 # if not(-1 < prev_y < N      )


# ------------------------------------------------------------------------------------

import sys
from pprint import pprint

# 상 -> y -= 1
# 하 -> y += 1

# 우 하 우상 우하
dy = [0, 1, -1, 1] 
dx = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

board = []

# 오목판 상황 입력
for _ in range(N):
    # 하나의 행을 입력 
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

# 무승부가 발생했을 때 출력하기 위한 값
answer = 0

# 이중 반복문 
for y in range(N):
    for x in range(N):
      
        # 검은색돌이나 흰색돌일때만 델타 탐색을 수행
        if board[y][x] == 1 or board[y][x] == 2:
      
            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 동일한 색의 돌의 개수 초기화(1)
                stone_count = 1
                
                # 다음 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    # 인덱스 조건, 범위를 벗어나면 탈출
                    if not(-1 < ny < N and -1 < nx < N):
                        break

                    # 같은 색(값) 돌인지 확인하는 조건, 다른 색 돌이면 탈출
                    if (board[y][x] != board[ny][nx]):
                        break
                    
                    # 같은 값이고 범위를 벗어나지 않으면 같은 색 돌의 수 + 1
                    stone_count += 1

                    # 같은 방향 다음 좌표를 탐색
                    ny = ny + dy[d]
                    nx = nx + dx[d]
                
                # 돌의 개수가 5개라면 
                if stone_count == 5:
                  
                    # 이전 좌표
                    # 기준 좌표(y, x) 에서 델타 값을 마이너스
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]

                    # 육목인지 판단
                    # 조건 1. 이전좌표가 범위를 벗어나면 오목
                    # if not(-1 < prev_y < N and -1 < prev_x < N):
                    
                    # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    # if board[y][x] != board[prev_y][prev_x]:
                    
                    # 조건 1과 조건2를 만족하면 오목이 완성
                    if not(-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                        # 현재 돌의 색 출력
                        print(board[y][x])
                        
                        # 현재 돌의 좌표를 출력
                        print(y + 1, x + 1)
                        
                        # answer 값 갱신
                        # 승패가 결정났기 때문에 answer 값 출력 X
                        answer = board[y][x]
                        

                        # 실제 코딩테스트에서 사용이 불가능한 방법
                        # exit(0)

# 전체를 반복했는데 무승부일 때 0 출력
if answer == 0:
    print(answer)