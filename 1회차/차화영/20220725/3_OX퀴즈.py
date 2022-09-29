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
            #i와 OX[i]를 answer 하나로 써도 됨
            point += 1
            # O가 나올 때마다 point 1씩 증가
            score = score + point
            # score에 point 추가
        elif OX[i] == 'X':
        # else: 
            point = 0
            # 연속된 O의 개수를 초기화(0)
    print(score)

    
    