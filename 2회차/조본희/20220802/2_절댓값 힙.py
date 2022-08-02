import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    number = int(input())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(number), number))