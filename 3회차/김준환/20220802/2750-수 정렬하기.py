import heapq

n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap,num)
for _ in range(n):
    print(heapq.heappop(heap))