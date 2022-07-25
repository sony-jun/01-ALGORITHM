# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
t = int(input())
for i in range(t):
    n = input()
    c = 0
    s = 0
    for j in n :
        if j == 'O':
            c += 1
            s+= c
        else :
            c = 0
    print(s)