import sys
import heapq
sys.stdin = open("2750.txt")

## 인풋 받고
t = int(input())
## 임시 리스트 초기화
temp_list = []

## 인풋 t 만큼 돌린다.
for i in range(t):
    ## 힙푸시 하면 자동 정렬을 아니지만 가장 작은 값이 제일 앞에 위치
    heapq.heappush(temp_list, int(input()))
#print(temp_list)

for i in range(t):
    ## 힙팝 하면 최소값이 차례대로 나온다.
    print(heapq.heappop(temp_list))