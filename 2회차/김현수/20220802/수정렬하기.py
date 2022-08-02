import sys
sys.stdin = open('수정렬하기.txt', 'r')
import heapq

N = int(input())
heap = []

for i in range(N):
    a = int(input())
    heapq.heappush(heap,a)

for i in range(N):
    print(heapq.heappop(heap))