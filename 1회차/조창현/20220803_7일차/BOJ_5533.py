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
pprint(score_trans)


one_matrix = []
for j in range(3):
    x = [] # 처음 등장한 값인지 판별하는 리스트
    alr_score = [] # 중복된 원소만 넣는 리스트
    for i in score_trans[j]:
        if i not in x: # 처음 등장한 원소
            x.append(i)
        else:
            if i not in alr_score: # 이미 중복 원소로 판정된 경우는 제외
                alr_score.append(i)
    one_list = list(set(x) - set(alr_score))
    print(one_list)
    one_matrix.insert(j, one_list)
print(one_matrix)

