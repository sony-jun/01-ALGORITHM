# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input())

for t in range(1, n+1):
    # ox를 문자열 리스트 형태로 저장
    ox = list(input())
    # 정답 변수 0으로 초기화
    sum = 0
    # 'O'가 연속으로 나올때까지 더할 변수 0으로 초기화
    tmp = 0

    # ox 리스트를 순회
    for i in ox:
        # ox가 'O'라면
        if i == "O":
            # tmp에 1씩 증가
            tmp += 1
            # 정답 변수에 tmp 더하기
            sum += tmp
        # xo가 'X'라면
        elif i == "X":
            # tmp를 0으로 초기화
            tmp = 0

    print(sum)