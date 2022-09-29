import sys
import heapq
sys.stdin = open("01_절댓값힙.txt", 'r')

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(heap, [abs(x), x]) # 키와 값처럼
    else:
        if len(heap) != 0:
            tmp = heapq.heappop(heap)
            print(tmp[1])
        else:
            print(0)