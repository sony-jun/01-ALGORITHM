# 11286.
"""
1. 접근방법
"""
import sys
sys.stdin = open("절댓값.txt")
import heapq

N = int(input())
queue = []
for _ in range(N):
    i = int(input())
    if i != 0:
        heapq.heappush(queue, [abs(i), i])
    if len(queue) != 0:
        if i == 0:
            heap = heapq.heappop(queue)
            print(heap[1])
    else:
        print(0)
