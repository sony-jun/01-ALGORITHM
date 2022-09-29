import sys
import heapq
sys.stdin = open("11286_절댓값힙.txt")

numbers = []
N = int(input())

for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(numbers, (abs(n), n))
    else:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers)[1])
