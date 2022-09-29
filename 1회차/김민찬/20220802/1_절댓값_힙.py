import sys

sys.stdin = open("1_절댓값_힙.txt")

import sys
import heapq

N = int(input())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))