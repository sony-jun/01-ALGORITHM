# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    # o을 만난다면 sum에 c를 더해주고 x를 만난다면 c를 1로 만들어주었다.
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)