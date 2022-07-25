# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for test_case in range(T):
    quiz = input()
    point = 0
    total = 0
    for char in quiz :
        if char == 'O':
            point += 1
            total += point
        else:
            point = 0 # X가 나오면 point 0으로 초기화
    print(total)