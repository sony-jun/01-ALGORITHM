# https://www.acmicpc.net/problem/8958
import sys


sys.stdin = open("3_OX퀴즈.txt")

a = []
cnt = 0
# 5번 반복함
T = int(input())
for test_case in range(T):
    # OX 값 입력
    A = input()
    # OX값 한번 확인
    #print(A)
    # OX 값 하나씩 대입
    for i in A:
        # O가 맞으면 1씩 증가
        if i == 'O':
            cnt += 1
            a.append(cnt)
        # O가 아니면 0으로 초기화
        else:
            cnt = 0
    print(sum(a))
    a = []
    cnt = 0

