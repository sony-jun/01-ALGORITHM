# from pprint import pprint

# m = 3
# n = int(input())
# matrix = [list(map(int,input().split())) for _ in range(n)]
# score_cnt = dict()
# for idx1 in range(m):
#     for idx2 in range(n):
#         score = matrix[idx2][idx1]
#         if score in score_cnt:
#             score_cnt[score] += 1
#         else:
#             score_cnt[score] = 1
#     for key in score_cnt:
#         if score_cnt[key] > 1:

#             matrix[idx1][matrix[idx1].index(key)]
# for idx2 in range(n):
#     print(sum(matrix[n]))


from pprint import pprint

m = 3
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

for idx1 in range(m):
    score_dic = dict()
    loser_score = []
    for idx2 in range(n):
        score = matrix[idx2][idx1]
        
        if score in score_dic:
            score_dic[score] += [1]
            if sum(score_dic[score][1:]) == 2:
                matrix[score_dic[score][0]][idx1] = 0
            matrix[idx2][idx1] = 0
        else:
            score_dic[score] = [idx2,1]


for idx2 in range(n):
    print(sum(matrix[idx2]))