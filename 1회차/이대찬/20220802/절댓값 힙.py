import sys
import heapq
sys.stdin = open('절댓값 힙.txt')

N = int(input())
heap = []
abs_ = []
t = []
for i in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
        heapq.heappush(abs_,abs(x))   

    elif x == 0:
        if not heap:
            print("0")
        else:
            while(1):
                if abs(heap[0]) == abs_[0]:
                    print(heapq.heappop(heap))
                    heapq.heappop(abs_)
                    break
                else:
                    heapq.heappush(t, heapq.heappop(heap))
                

        if len(heap) != len(abs_):
            while(t):
                heapq.heappush(heap, heapq.heappop(t))


 