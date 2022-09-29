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

m = 3                # 열 3개
n = int(input())     # 행 n개
matrix = [list(map(int,input().split())) for _ in range(n)]
# [[100, 98, 98],
#  [100, 97, 92],
#  [63, 89, 63],
#  [99, 99, 99],
#  [89, 97, 98]]

for idx1 in range(m):        # 가로(열)탐색 _ 상위
    score_dic = dict()       # 점수 딕셔너리. 키 = 점수 
                             #               값 = [처음 점수 나온 인덱스, 1,1,1, ...]

    for idx2 in range(n):             # 세로(행)탐색 _ 하위
        score = matrix[idx2][idx1]    # 매트릭스에서 찾아서 score에 점수 저장
        
        if score in score_dic:                # 이미 나온 점수인지 검색
            score_dic[score] += [1]           # 카운트 추가
            if sum(score_dic[score][1:]) == 2:         # 카운트 합이 2 이면 => 앞에 중복점수 제거
                matrix[score_dic[score][0]][idx1] = 0  # 매트릭스에서 해당 점수의 
            matrix[idx2][idx1] = 0                     # 첫 인덱스로 접근해 0점 값 변경

        else:
            score_dic[score] = [idx2,1]       # 처음 나온 점수면 딕셔너리에  점수 :[현재 인덱스,1]


for idx2 in range(n):
    print(sum(matrix[idx2]))