# https://www.acmicpc.net/problem/8958

import sys
sys.stdin = open('3_OX퀴즈.txt', 'r')

T = int(input())

for i in range(T):
    cnt = 0
    total = 0
    string = input()
    for i in string:
        if i == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)