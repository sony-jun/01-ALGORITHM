import sys
sys.stdin = open('B2750.txt')

import heapq
N = int(input())
h = []
for i in range(N):
    heapq.heappush(h, int(input()))

for l in range(N):
    print(heapq.heappop(h))