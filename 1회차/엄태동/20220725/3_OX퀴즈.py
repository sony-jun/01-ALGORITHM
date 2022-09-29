# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(T):
    ox_list=list(input())
    score = 0
    num = 1
    for i in range(len(ox_list)):
        if ox_list[i] == 'O':
            score += num
            if i<len(ox_list)-1:
                if ox_list[i] == ox_list[i+1]:
                    num += 1
                else:
                    num = 1
    print(score)