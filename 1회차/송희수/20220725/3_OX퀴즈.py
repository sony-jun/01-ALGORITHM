# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(1,T+1):
    oxstr = list(str(input()))
    sum = 0
    c = 1
    for i in oxstr:
        if i == 'O':
            # c를 더하는 개념이 중요하다.
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
    

    