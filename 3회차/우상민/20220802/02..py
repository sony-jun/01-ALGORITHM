# 백준 절댓값 힙
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
import heapq
P = []
M = []
for i in range(int(input())):
    N = int(input())
    if N > 0:
        heapq.heappush(P, N)
    elif N < 0:
        heapq.heappush(M, -N)
    else:
        if not M:
            if not P:
                print(0)
            else:
                print(heapq.heappop(P))
        elif not M:
            print(-heapq.heappop(M))
        else:
            num_1 = -heapq.heappop(M)
            num_2 = heapq.heappop(P)
        
            if abs(num_1) > abs(num_2):
                print(num_2)
                heapq.heappush(M, -num_1)
            else:
                print(num_1)
                heapq.heappush(P, num_2)

import heapq

n = int(input())
q = []

for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(q, (abs(a), a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
