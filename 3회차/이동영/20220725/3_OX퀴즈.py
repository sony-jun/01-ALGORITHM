# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1,T+1):
    N = list(input())
    result = 0
    cnt = 1

    for j in N:
        if j == 'O':
            result += cnt
            cnt += 1
            
        elif j == 'X':
            cnt = 1  
    print(result)