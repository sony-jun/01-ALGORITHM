# https://www.acmicpc.net/problem/11286

import sys
input = sys.stdin.readline

import heapq # heap push, pop을 하기 위한 heapq import

N = int(input()) # 개수
heaps = [] # 절대값이 가장 작은값을 출력하기 위한 heap

for i in range(N):
    number = int(input())
    if number != 0: # 입력받은 값이 0이 아닐때 
        heapq.heappush(heaps, (abs(number), number)) # 절대값과 수를 튜플로 넣는다.
    else: # 입력받은 값이 0일때
        if len(heaps) == 0: # 비어있을 경우 0 출력
            print(0)
        else:
            print(heapq.heappop(heaps)[1]) # [1]번째 인덱스의 값을 출력한다.