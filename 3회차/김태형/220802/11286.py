# 입력에서 0이 주어진 회수만큼 답을 출력한다.
# 우선순위 que

from heapq import heappop


N = int(input())
Q = []
for i in range(N):
    x = int(input())
    if x!=0:
        Q.append(x)
    else:
        print("0" if len(Q)==0 else heappop((Q)))