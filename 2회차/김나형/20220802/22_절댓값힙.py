# import heapq
# import sys
# sys.stdin = open ("22_절댓값힙.txt")

# N=int(sys.stdin.readline())
# heap=[]
# for _ in range(N):
#   x=int(sys.stdin.readline())
#   if x==0:
#     if heap:
#       print(heapq.heappop(heap)[1]) # heappop 가장 작은 원소값을 제거하고 리턴한다. 두번 째 인자가 기존 값이므로 [1]을 넣어 찾아준다.
#     else:
#       print(0)
#   else:
#     heapq.heappush(heap, (abs(x),x)) # heappush(), 첫번째 인자는 원소를 추가할 대상 리스트, 두번째 인자는 추가할 원소 // 두번째 인자에 절댓값과 기존 값을 튜플로 추가하여 절댓값순으로 정렬


import heapq
import sys
sys.stdin = open ("22_절댓값힙.txt")

T = int(sys.stdin.readline())
heap = []
for _ in range(T):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, (abs(n),n))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)