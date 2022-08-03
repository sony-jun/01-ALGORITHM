import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1]) # 힙 리스트에 가장 작은 튜플 출력, 뒤에 있는 튜플 중 인덱싱 1값 원래 값을 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x),x)) # 0이 아니면 절대값, 원래값을 쌍으로 넣어주어 절대값 기준으로 정렬