# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

number = int(input())

for i in range(0,number): #테스트 케이스의 개수만큼 반복
    result = 0          # 결과값 초기화
    a=input().split('X') #X를 기준으로 O만 추출

    for i in range(0,len(a)):
        score = 1               #O의 점수 초기화
        plus = a[i].count('O') # 연속된 O의 갯수 구하기

        for i in range(0,plus): #연속된 O의 개수만큼 반복
               result+=score
               score+=1        #연속된 O의 점수

    print(result)

