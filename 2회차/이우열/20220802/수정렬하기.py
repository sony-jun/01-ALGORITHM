import heapq

n = int(input())

heap = []

for i in range(n):
    num = int(input())

    heapq.heappush(heap, num)

for i in range(n):
    print(heapq.heappop(heap))
