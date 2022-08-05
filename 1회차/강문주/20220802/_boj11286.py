import sys
import heapq
N = int(input())
minusq = [] # 음수를 넣을 큐
absolq = [] # 양수를 넣을 큐
 
for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a < 0:
        heapq.heappush(minusq, -a) # 절댓값작은게 앞으로
    elif a > 0:
        heapq.heappush(absolq, a) # 양수는 그대로
    else: # 0이 입력되면
        if not minusq: # 음수큐가 비었니?
            if not absolq: # 양수큐도 비었니?
                print(0) #그럼 없는거야
            else: #양수큐는 있나봐?
                print(heapq.heappop(absolq)) #양수큐최소출력
        elif not absolq: # 음수큐는 있는데 양수큐는 없다고?
            print(-heapq.heappop(minusq)) # 그럼음수큐에서빼

        else: # 둘다차있으면
            tmp1 = -heapq.heappop(minusq) #\음수큐\랑
            tmp2 = heapq.heappop(absolq) #양수큐랑 각 최솟값

            if abs(tmp1) > abs(tmp2): # 비교해
                print(tmp2)
                heapq.heappush(minusq, -tmp1)

            else:
                print(tmp1)
                heapq.heappush(absolq, tmp2)