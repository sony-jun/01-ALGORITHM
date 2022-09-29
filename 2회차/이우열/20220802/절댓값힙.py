import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    number = int(input())
    if number != 0:
        heapq.heappush(heap, (abs(number), number))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
