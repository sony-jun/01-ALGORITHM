import heapq
import sys

sys.stdin = open("절댓값 힙.txt")

heap = []
N = int(input())

for _ in range(N):
    n = int(sys.stdin.readline())
        
    if n:
        heapq.heappush(heap,(abs(n), n))
    else : 
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)