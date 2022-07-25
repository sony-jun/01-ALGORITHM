# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

a = int(input()) # a에 첫줄 값 받아오기
for i in range(a): # 총 5번 반복
    b = list(str(input())) # b 에 리스트 첫 줄 값
    cnt = 1 # 시작 점수는 1점
    sum = 0 # 전부 합은 sum
    for i in b: # 더하기 계산을 리스트 b 의 길이 만큼 반복
        if i == 'O': # 리스트 i 가 'O'과 같다면
            sum += cnt # sum 에 cnt 값 더하기
            cnt += 1 # 그리고 cnt 값을 1 증가시킨다
        else: # 'O'가 아니라면
            cnt = 1 # cnt 값을 1로 초기화
    print(sum) # sum 값을 프린트 한다