# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("./3회차/신윤식/20220725/3_OX퀴즈.txt")


# 1. 리스트 활용
T = int(input())

for i in range(T):

    wrong_correts = input()
    count = 0
    lst = []

    for wrong_corret in wrong_correts:
        if wrong_corret == 'O':
            count+=1
            lst.append(count)
        elif wrong_corret == 'X':
            count = 0

    print(sum(lst))

    
# 2. 변수 활용
n = int(input())
num=1
total=0

for i in range(n):
    x = input()
    for j in x:
        if j == 'O':
            total += num
            num += 1
        elif j == 'X':
            num = 1
    print(total)
    num = 1
    total=0