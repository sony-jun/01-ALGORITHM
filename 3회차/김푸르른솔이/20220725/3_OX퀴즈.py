# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    score = 0
    sum_score = 0
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