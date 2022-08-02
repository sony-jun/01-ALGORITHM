import sys
input = sys.stdin.readline

import heapq

heap = []

N = int(input())
for _ in range(N):
    n = int(input())

    # n이 0이 아니면
    if n != 0: 
        # 튜플로 두번째 인자를 받아서 heappush 한다.
        # heap은 튜플 중 첫번째 값 기준으로 정렬함.
        heapq.heappush(heap,(abs(n), n))
    
    # n이 0이라면
    else:
        # heap 안에 뭐가 있을 때
        if len(heap) != 0:
            # 튜플의 두번째 값을 프린트
            print(heapq.heappop(heap)[1])

        # heap 안에 아무것도 없을 때
        else:
            print(0)


