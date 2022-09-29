import heapq

n = int(input())
heap = []

for i in range(n):
    number = int(input())
    heapq.heappush(heap, number)

for i in range(n):
    print(heapq.heappop(heap))