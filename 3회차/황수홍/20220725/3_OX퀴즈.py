# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

q = int(input())

for ii in range(q) :
    a = input()
    score = 0
    cnt = 0
    for i in range(len(a)) :
        if a[i] == "O" :
            cnt += 1
            score += cnt
        elif a[i] == "X":
            cnt = 0
    print(score)