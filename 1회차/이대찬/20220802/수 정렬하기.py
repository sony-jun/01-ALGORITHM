import sys
import heapq
sys.stdin = open('수 정렬하기.txt')

N = int(input())
heap = []
result = []
for i in range(N): 
    heapq.heappush(heap, int(input()))
 
for i in range(N):
    result.append(heapq.heappop(heap))
    print(result[i])
      
    

 

