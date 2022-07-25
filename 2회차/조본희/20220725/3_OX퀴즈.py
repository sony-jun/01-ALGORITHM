# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for test_case in range(1, T +1):
    OX = input()
    count = 0
    answer = 0
    for i in OX:
        if i == 'O':
            count += 1
            answer += count
        if i == 'X':
            count = 0
    
    print(answer)