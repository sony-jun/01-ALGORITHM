import heapq

heap = []

T = int(input())
for _ in range(T):
    num = int(input())
    heapq.heappush(heap,num)


while len(heap) != 0:
    answer = heapq.heappop(heap)     
    print(answer)

