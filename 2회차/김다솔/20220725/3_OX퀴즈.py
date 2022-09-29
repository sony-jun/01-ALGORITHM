# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

# o 인 동안 n+1 -> while

T = int(input())
for i in range(1, T+1):
    ox = list(input())
    # print(ox)
    count = 0 # 연속된 횟수 
    points = 0 # 점수 합계
    for i in ox: # ox 하나씩 반복될 동안 
        if i == 'O': # o면 카운트해서 합계에 +1 +2... 
            count += 1
            points = points + count
        else: # x면 카운트 다시 시작
            count = 0 
        
    print(points)
        