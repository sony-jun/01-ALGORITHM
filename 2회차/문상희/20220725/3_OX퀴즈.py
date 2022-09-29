# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for i in range(T):
    each_line = input()
    total_point = 0
    point = 0
    for j in range(len(each_line)):
        if each_line[j] == 'O' :
            point += 1
            total_point += point
        else:
            point = 0
    print(total_point)
