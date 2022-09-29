# https://www.acmicpc.net/problem/2846

import sys

sys.stdin = open("2_오르막길.txt", "r")

n = int(input())
p = list(map(int,input().split()))  # 입력값을 리스트에 담아준다.
l = []                              # 오르막길의 높이를 담을 리스트
h = 0                               # 오르막길의 높이

for i in range(n-1):                # 인덱싱으로 비교를 위한 반복문
    if p[i] < p[i+1]:               # 만약 오르막길이라면
        h += p[i + 1] - p[i]        # 높이 차이를 h에 할당
    if p[i] >= p[i+1]:              # 만약 내리막길이라면
        l.append(h)                 # 리스트에 높이를 추가
        h = 0                       # 높이 차이 초기화
l.append(h)                         # 마지막 오르막길 높이 추가

print(max(l))
        