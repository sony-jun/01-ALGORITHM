# https://www.acmicpc.net/problem/8958

# O는 문제를 맞은 것, X는 문제를 틀린 것
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
# 예 : OOXXOXXOOO 의 10번 문제 점수는 3이다.
# OX 퀴즈의 결과가 주어졌을 때 점수는 구하는 프로그램 작성

# 첫째 줄에 테스트 케이스의 개수가 주어짐
# 각 테스트 케이스는 한 줄로 이루어져 있고
# 길이가 0보다 크고 80보다 작은 O, X로만 구성된 문자열

import sys

sys.stdin = open("3_OX퀴즈.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    OX = input()
    num = int()
    result = int()

    for i in  OX:
        if i == 'O':
            # i 가 O인 경우 1씩 더함
            num += 1
            # 1씩 더한 num 값을 더해줌
            result += num
        else: # i 가 X인 경우 값을 더하지 않음
            i != 'O'
            num = 0
    print(result)

    # 결과값을 출력하고 result와 num을 0으로 초기화
    result = 0
    num = 0