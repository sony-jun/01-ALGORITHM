# 1.문제를 읽고 이해한다

# 최소 힙에 문자와 비슷하다
# 0이 아니라면 배열에 추가하고 0이라면 배열에서 절댓값을 출력한다


# 2. 문제를 익숙한 용어로 재정의한다
# heap = []
# n !=0
# heapq.heappush()
# len(heap) ==0:
# heapq.heappop()

# 3. 어떻게 해결할지 계획을 세운다

# 배열을 받을 heap을 리스트화 시키고
# 테스트케이스 for문 작성 후
# 만약 0이 아니라면
# 배열에 추가해주는데 절대값과 원래값에서 비교한다
# 0이라면 0을 출력하고 아니라면 [1]번 요소를 출력해 원래 값을 출력해라

# 프로그램으로 구현한다

import heapq
import sys

sys.stdin = open('_절댓값.txt')
heap = []
N = int(input())
for _ in range(N):
    n = int(sys.stdin.readline())
    if n !=0:
        heapq.heappush(heap, (abs(n),n))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

# 어떻게 풀었는지 돌아보고, 개선할 방법이 있는지 찾아본다

