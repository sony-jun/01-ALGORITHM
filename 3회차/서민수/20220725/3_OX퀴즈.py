
# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

# OX중 연속되면 1+2+3+4 연속으로 점수 획득
# X는 0이 되야 하고 O는 1이 되야함
t = int(input())


for i in range(t):
    # ox를 받아 줄 함수
    c = input()
    cnt = 0 # 숫자의 합을 더해줄 카운트
    result = 0 # 결과값
    # 스코어에 j가 있다면
    for j in c:
        # 만약 J가 "O"라면
        if j == "O":
            # 카운트 1씩 더해줘라
            cnt += 1  
            # result값은 cnt랑 더해줘라
            result += cnt        
        else:
            # X가 나온다면 0으로 초기화시켜라
            cnt = 0
    print(result)
        
