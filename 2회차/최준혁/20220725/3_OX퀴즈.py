# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("/Users/mac/Desktop/TIL/01-ALGORITHM/2회차/최준혁/20220725/3_OX퀴즈.txt")

T_case = int(sys.stdin.readline())
cnt = 0
score = 0
for case in range(T_case): # 테스트 케이스의 횟수
    res = sys.stdin.readline() # OX퀴즈 내역
    for OX in res: 
        if OX == "O": # 퀴즈 내역 안에 O가 있으면
            cnt += 1 # 카운트 증가
            score += cnt # 카운트를 누적
        elif OX == "X": # X면?
            cnt = 0 # 초기화!
    print(score) # 출력
    cnt = 0 # 초기화 
    score = 0
