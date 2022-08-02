# 입력에서 0이 주어진 회수만큼 답을 출력한다.
# 우선순위 que

from heapq import heappop, heappush
import sys

Q = []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        heappush(Q,(abs(x),x))
    if x==0:
        print("0" if len(Q)==0 else heappop(Q)[1])    