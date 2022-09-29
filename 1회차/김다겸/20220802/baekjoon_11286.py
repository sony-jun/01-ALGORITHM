import heapq
import sys

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    # 연산에 대한 정보
    input_ = int(input())

    # input이 0이 아니면
    if input_ != 0:
        # heap 리스트에 (input의 절댓값, input) 튜플 형태로 heapq로 추가하기
        # input의 절댓값을 기준으로 제일 작은 수가 맨 앞으로 정렬
        heapq.heappush(heap, (abs(input_), input_))
    # input이 0이 아닌 정상적인 숫자라면
    else:
        # heap에 남아있는 요소가 없으면
        if len(heap) == 0:
            # 0 출력
            print(0)
        # heap에 남아있는 요소가 있으면
        else:
            # heap에서 튜플의 1인덱스 값을 출력
            print(heapq.heappop(heap)[1])