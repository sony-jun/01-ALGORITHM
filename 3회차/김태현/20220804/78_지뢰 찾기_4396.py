from pprint import pprint

import sys
sys.stdin = open("78_지뢰 찾기_4396.txt", "r")

# 입력
# 첫 N줄: 지뢰 설계도 # bomb_matrix
# 다음 N줄: 사용자가 클릭한 위치 # click_matrix

# 출력
# 클릭/비클릭한 리턴 값 # number_matrix

# 클릭한 위치 1개 + 주변 8개의 인덱스값 가져옴
# 클릭한 위치에 지뢰 있으면, 모든 지뢰 위치 "*"표
# 8개 인덱스 안에 지뢰 있으면, 개수 만큼 표시

# [0, 0] [0, 1] [0, 2]
# [1, 0] [1, 1] [1, 2]
# [2, 0] [2, 1] [2, 2]

N = int(input())

# 폭탄 매트리스
bomb_matrix = []
for _ in range(N):
    bomb_matrix.append(input())

# 클릭 매트릭스
click_matrix = []
for _ in range(N):
    click_matrix.append(input())

# 숫자 매트릭스 (출력)
number_matrix = [["."] * N for _ in range(N)]


# print(bomb_matrix, "bomb")
# print(click_matrix, "click")

for i in range(N):
    for j in range(N):
        # print(i, j, "i", "j") ##############################
        # 지뢰 밟았을 때
        if bomb_matrix[i][j] == click_matrix[i][j]:
            True # 지뢰 인덱스 구해서 number_matrix에 표시

        # 지뢰 안 밟았을 때 # 주변 8개 순회 # 지뢰 개수 cnt
        else:
            cnt = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    # print(ii, jj, "ii", "jj") ################
                    try:
                        if bomb_matrix[ii][jj] == "*":
                            cnt += 1
                    except IndexError:
                        print(ii, jj, "error")
                        continue
            number_matrix[i][j] = cnt

pprint(bomb_matrix)
pprint(number_matrix)

# for i in range(N): # 8 x 8 click_matrix 순회, 
#     for j in range(N):
#         if click_matrix[i][j] == "x": # 클릭한 위치 발견하면
#             if i, j = q, w
            
#             cnt = 0
#             for a in range(i-1, i+2): # 클릭 위치 + 주변 8개 위치 순회,
#                 for b in range(j-1,j+2):
#                     if map_matrix[i][j] == "*": # 클릭한 위치 i,j에 지뢰가 있으면
#                             True
#                     elif map_matrix[a][b] == "*": # 8개 안에 있으면, cnt += 1
#                         cnt += 1
#             number_matrix[i][j] = cnt
          

