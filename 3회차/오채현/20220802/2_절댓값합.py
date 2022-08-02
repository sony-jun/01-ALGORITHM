# import heapq

# n = int(input())
# heap = []

# for i in range(n):
#     x = int(input())
#     if x != 0:
#         heapq.heappush(heap, (abs(x), x))
#         print(heap)
#     else:
#         if not heap:
#             print(0)
#         else:
#             print(heapq.heappop(heap[1]))

#------
import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            #x가 0인 경우 답을 출력해야 하므로 heap에 원소가 있는 경우 가장 작은 값의 튜플 중 원래 x 값을 제거하고 출력한다
            print(heapq.heappop(heap)[1])
        else:
            #x가 0인 경우 중 heap에 원소가 없을 경우 0을 출력
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
        #x가 0이 아닌경우에는 힙에 x의 절댓값과 x를 튜플로 묶어서 삽입

#런타임 에러... 해결pypy3