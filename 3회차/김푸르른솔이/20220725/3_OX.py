import sys

sys.stdin = open("3_OX.txt")

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    score = 0 # 연속된 0의 개수
    sum_score = 0 # 점수의 총합
    for ox in s:
        if  ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

    
# a = int(input())
# for i in range(a):
#     b = input()
#     score = 0
#     sumscore = 0
#     for j in b:
#         if j == 'O':
#             score += 1
#         else:
#             score = 0
#         sumscore += score
#     print(sumscore)