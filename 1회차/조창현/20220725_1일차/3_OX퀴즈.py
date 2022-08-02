# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = input()
score = 0

for case in range(1, (int(T) + 1)):
    score = 0
    weight = 0
    ans = input()
    for i in ans:
        if i == 'O':
            #print('o')
            weight += 1
            score += weight
        else:
            weight = 0
    print(score)
    