import sys
import heapq

# 정수 x 담을 리스트
min_heap = []

# 입력 개수 N 받기
N = int(input())

# N개의 줄만큼 입력 받기
for _ in range(N):
    x = int(sys.stdin.readline())
    # 0 아닐때, 힙에 (절댓값, 원래값) 같이 넣어주기
    if x != 0:
        heapq.heappush(min_heap, (abs(x), x))
    # 0 일때 
    else:
        # 비어 있는 경우 0 출력
        if len(min_heap) == 0:
            print(0)
        # 비어 있지 않으면, 뒤에 있는 원래 값 출력
        else:
            print(heapq.heappop(min_heap)[1])



