# from pprint import pprint
# import sys
# sys.stdin = open('2615.txt')

# om = [list(map(int, input().split())) for i in range(19)]
# #pprint(om)

# dx = [-1, -1, -1, 0, 1, 1, 1, 0]
# dy = [1, 0, -1, -1, -1, 0, 1, 1]

# om_one = []
# for x in range(19):
#     for y in range(19):
#         # for i in range(8):
#         #     if 0 <= x + dx[i] < 19 and 0 <= y + dy[i] < 19:
#         #         x = x + dx[i]
#         #         y = y + dy[i]
#         if om[x][y] == 1:
#             om_one.append([x, y])


# #pprint(om_one)
# one_xlist = []
# one_ylist = []
# one_fx = []
# one_fy = []
# for r in range(len(om_one)): ## r 은 좌표야
#     for i in range(8):
#         one_xlist = []
#         one_ylist = []
#         one_cnt = 1
#         #print(f'1 시작 {om_one[r]}')
#         x = om_one[r][0] + dx[i]    ## 좌표
#         y = om_one[r][1] + dy[i]    ## 좌표
#         #print(x, y)
#         if [x, y] in om_one:
#             one_xlist.append(int(om_one[r][0]))
#             one_ylist.append(int(om_one[r][1]))
#             one_cnt += 1
#             #print(f'1이야 {[x, y]}')
#             dirct = i
#             one_xlist.append(int(x))
#             one_ylist.append(int(y))
#             for j in range(len(om_one)):
#                 x = x + dx[dirct]
#                 y = y + dy[dirct]
#                 if [x, y] in om_one:
#                     one_cnt += 1
#                     #print(f'또 1이야 {[x, y]}')
#                     one_xlist.append(int(x))
#                     one_ylist.append(int(y))
#                     if one_cnt == 5:
#                         #print('1')
#                         #print(one_xlist)
#                         #print(one_ylist)
#                         one_fx = one_xlist
#                         one_fy = one_ylist
                    




# om_two = []
# for x in range(19):
#     for y in range(19):
#         if om[x][y] == 2:
#             om_two.append([x, y])

# two_xlist = []
# two_ylist = []
# two_fx = []
# two_fy = []
# for r in range(len(om_two)): ## r 은 좌표야
#     for i in range(8):
#         two_xlist = []
#         two_ylist = []
#         two_cnt = 1
#         #print(f'1 시작 {om_one[r]}')
#         x = om_two[r][0] + dx[i]    ## 좌표
#         y = om_two[r][1] + dy[i]    ## 좌표
#         #print(x, y)
#         if [x, y] == om_two[r + 1]:
#             two_xlist.append(int(om_two[r][0]))
#             two_ylist.append(int(om_two[r][1]))
#             two_cnt += 1
#             #print(f'1이야 {[x, y]}')
#             dirct = i
#             two_xlist.append(int(om_two[r + 1][0]))
#             two_ylist.append(int(om_two[r + 1][1]))
#             for j in range(len(om_two)):
#                 x = x + dx[dirct]
#                 y = y + dy[dirct]
#                 if [x, y] in om_two:
#                     two_cnt += 1
#                     #print(f'또 1이야 {[x, y]}')
#                     two_xlist.append(int(x))
#                     two_ylist.append(int(y))
#                     if two_cnt == 5:
#                         #print('1')
#                         print(two_xlist)
#                         print(two_ylist)
#                         two_fx = two_xlist
#                         two_fy = two_ylist

# if len(one_fx) < 5 and len(two_fx) < 5:
#     print('0')

# elif len(one_fx) == 5:
#     print('1')
#     y_min = min(one_fy)
#     y_ind = one_fy.index(y_min)
#     print(one_fx[y_ind] + 1, one_fy[y_ind] + 1)

# elif len(two_fx) == 5:
#     print('2')
#     y_min = min(two_fy)
#     y_ind = two_fy.index(y_min)
#     print(two_fx[y_ind] + 1, two_fy[y_ind] + 1)


##################################################
################### 강사님 ##################
##################################################

import sys
sys.stdin = open('2615.txt')

dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]

black = 1
white = 2
n = 19

board = []
answer = 0

for _ in range(n):
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

for y in range(n):
    for x in range(n):
        if board[y][x] == 1 or board[y][x] == 2:
            for d in range(4):
                stone_count = 1

                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    if not(-1 < ny < n and -1 < nx < n):
                        break
                    if not(board[y][x] == board[ny][nx]):
                        break

                    stone_count += 1

                    ny = ny + dy[d]
                    nx = nx + dx[d]

                if stone_count == 5:
                    prey_y = y - dy[d]
                    prey_x = x - dx[d]
                    
                    if not(-1 < prey_y < n and -1 < prey_x < n) or board[y][x] != board[prey_y][prey_x]:
                        answer = board[y][x]
                        print(answer)
                        print(y + 1, x + 1)

if answer == 0:
    print(answer)


############################################################
############## 강사님 ######################################
############################################################

import sys
from pprint import pprint
sys.stdin = open("2615.txt") 

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