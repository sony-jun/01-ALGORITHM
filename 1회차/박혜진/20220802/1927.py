import heapq

N  = int(input())
heap = []
# heapq.heapify(heap)

for _ in range(N) :
    n = int(input())
    
    if n != 0 :
        heapq.heappush(heap, n)
    else :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap))

# 정답 코드 
import sys
import heapq

numbers = int(input())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
