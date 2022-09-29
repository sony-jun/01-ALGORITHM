# https://www.acmicpc.net/problem/7568
import sys
sys.stdin = open("7568.txt")

T = int(input())
body = [] # 몸무게와 키를 저장할 리스트

for _ in range(T): # _는 값을 무시하고 싶을 때 사용
    x, y = map(int, input().split())
    body.append((x, y))

for i in body:
    rank = 1 # 현재 i가 1등
    for j in body:
        if i[0] < j[0] and i[1] < j[1]: # i보다 j의 키와 몸무게가 더 크다면
            rank += 1 # 덩치 등수가 하나 밀려날 것
    print(rank, end = " ") # print 위치 주의!!