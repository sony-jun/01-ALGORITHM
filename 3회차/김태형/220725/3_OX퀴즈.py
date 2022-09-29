# https://www.acmicpc.net/problem/8958
# import sys

# sys.stdin = open("3_OX퀴즈.txt")

n = int(input())
score_gross = 0
score = 0
for i in range(n):
    check_o = input()
    for j in check_o:
        if j=='O':
            score_gross+=1
            score+=score_gross
        elif j=="X":
            score_gross=0
print(score)