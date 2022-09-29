# 백준 11286

import heapq
import sys
sys.stdin = open('절댓값힙.txt', 'r')

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    # num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)