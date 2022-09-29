import heapq
import sys

sys.stdin = open('절대값힙_input.txt')

# X의 개수 입력
N = int(input())

# heap
heap = []

#cnt
cnt = []

for i in range(N):
    # x 입력
    x = int(input())
    
    # 만약 x가 0이 아니라면 
    if x != 0:
        heapq.heappush(heap, (abs(x),x))
    # x가 0이면 가장 작은 값 출력하고 삭제
    elif x == 0:
        heapq.heappop(heapq.heappop(0))
        # 절대값이 가장 작은 값 제거
    if len(heap) == 0:
        print(0)