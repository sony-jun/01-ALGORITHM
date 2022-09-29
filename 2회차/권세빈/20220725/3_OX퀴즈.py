# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
t = int(input())
for test_case in range(1,t+1):
    q = list(input())       # 리스트 변환
    cnt = 0                 
    score = 0
    for i in q:             # 리스트에 있는 값을 하나하나 비교하기 위한 반복문
        if i == 'O':        # 만약 O라면
            cnt += 1        # 카운트 1씩 증가
            score += cnt    # 카운트를 점수에 반영
        else:               # O이 아니라 X라면
            cnt = 0         # 카운트 0으로 초기화
    print(score)
