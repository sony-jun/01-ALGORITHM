# https://www.acmicpc.net/problem/11286

# x != 0이면 비어있는 배열에 x를 추가, x=0이면 배열에서 가장 작은값이 출력 후 삭제

import heapq
import sys
input = sys.stdin.readline

t = int(input())

bea_ = []
out = 0
for _ in range(t):
    x =int(input())
    if x != 0:
        heapq.heappush(bea_, (abs(x), x))
    else: 
        if len(bea_) == 0:
            print('0')
        else:
            print(heapq.heappop(bea_)[1])