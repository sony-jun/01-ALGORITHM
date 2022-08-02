import heapq
n = int(input())
result = []
for i in range(n):
    num = int(input())
    heapq.heappush(result,num)
for i in range(n):
    print(heapq.heappop(result))