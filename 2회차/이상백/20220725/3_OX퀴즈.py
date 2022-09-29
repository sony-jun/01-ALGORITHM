# https://www.acmicpc.net/problem/8958
# import sys

# sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for test in range(1, T+1):
    sum = 0 # 초기값
    result = 0 # 결과값
    ox = input()
    for i in ox:
        if i == 'O':
            sum += 1 # O가 연속되면 1씩 증가
            result += sum # O값을 저장
        else:
            sum = 0 # X가 나올 경우 sum 0으로 초기화
    print(result)