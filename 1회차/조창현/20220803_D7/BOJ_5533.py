from pprint import pprint
import sys

sys.stdin = open("5533.txt")

n = int(input())
sum_n = [0 for _ in range(n)]

score_mat = [list(map(int, input().split())) for i in range(n)]

#pprint(score_mat)

row_temp = []
score_trans = []
for col in range(3):
    row_temp = []
    for row in range(n):
        row_temp.append(score_mat[row][col])
    score_trans.insert(col, row_temp)
    #pprint(cast_trans)
#pprint(score_trans)

######  중복을 너무 복잡하게 처리 하려던 케이스

# one_matrix = []
# for j in range(3):
#     x = [] # 처음 등장한 값인지 판별하는 리스트
#     alr_score = [] # 중복된 원소만 넣는 리스트
#     for i in score_trans[j]:
#         if i not in x: # 처음 등장한 원소
#             x.append(i)
#         else:
#             if i not in alr_score: # 이미 중복 원소로 판정된 경우는 제외
#                 alr_score.append(i)
#     one_list = list(set(x) - set(alr_score))
#     print(one_list)
#     one_matrix.insert(j, one_list)
# print(one_matrix)
score_ind = [0] * n
for r in range(3):
    for c in range(n):
        #print(score_trans[r])
        #print(score_ind[c])
        if score_trans[r].count(score_trans[r][c]) == 1:
            score_ind[c] += score_trans[r][c]

for i in range(n):
    print(score_ind[i])


####################################################################
##############  수람님  ####################################################
#####################################################

# import sys

# # M: 가로 행
# # N = 3 # 세로 열 고정
# M = int(input())

# card_matrix = [list(map(int, input().split())) for i in range(M)]

# score_list = []
# for j in range(3):
#     temp_list = []
    
#     for i in range(M):
#         temp_list.append(card_matrix[i][j]) 
        
#     score_list.append(temp_list)

# for i  in range(M):
#     result = 0
#     for j in range(3):

#         if score_list[j].count(card_matrix[i][j]) > 1:
#             result += 0
#         else:
#             result += card_matrix[i][j]
#     print(result)