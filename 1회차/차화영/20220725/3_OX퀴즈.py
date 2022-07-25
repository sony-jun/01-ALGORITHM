# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())

for test_case in range(1, T+1):
    OX = input()
    score = 0 
    point = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            point += 1
            # O가 나올 때마다 point 1씩 증가
            score = score + point
            # score에 point 추가
        else:
            point = 0
            # X가 나오면 point가 0이라 다시 O가 나오면 1부터 시작해야 됨
    print(score)

    
    