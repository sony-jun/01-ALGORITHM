# 1. 배열에 정수 x (x ≠ 0)를 넣는다.
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
#    절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 
#    그 값을 배열에서 제거한다.
# 3. 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N): # N만큼 반복
    x = int(input())
    if x != 0: # x가 0이 아닐때
        heapq.heappush(heap, [abs(x), x]) # x의 절대값과 x를 묶어서 푸시
        #print(heap)
    else:
        if len(heap) == 0: # heap의 길이가 0 일때
            print(0)       # 0출력
        else:
            print(heapq.heappop(heap)[1]) # 리스트로 묶은 절대값과 x값 중 x를 출력
            #print(heap)



