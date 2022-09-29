N = int(input())

score = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    sum = 0
    for j in range(3):
        a = score[i][j]
        check = 1
        for k in range(N):
            if i == k:
                continue
            if a == score[k][j]:
                check = 0
                break
        if check == 1:
            sum += a
    print(sum)

# 코드리뷰 풀이
# list_ = [[100, 99, 98],
#         [100, 97, 92],
#         [63, 89, 63],
#         [99, 99, 99],
#         [89, 97, 98],
#         ]
# score_list = [0] * 5

# col_list = []
# # 리스트를 90도 회전
# for x in range(3):
#     col = []
#     for y in range(5):
#         col.append(list_[y][x])

#     col_list.append(col)

# # 친구들의 점수 리스트
# score_list = [0] * 5
# for x in range(3):
#     col = col_list[x]
#     for y in range(5):
#         # 친구의 점수
#         score = col[y]
#         # 친구의 점수가 리스트에서 1개일때
#         if col.count(score) == 1:
#             # 친구의 점수 증가
#             score_list[y] += score
# print(score_list)