import sys
sys.stdin = open("2_절댓값힙.txt")
import heapq

# import sys
# input = sys.stdin.readline

heap =[]

N = int(input())

for tc in range(1, N+1):
    x = int(input())
    if x !=0:
        heapq.heappush(heap, (abs(x),x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)


