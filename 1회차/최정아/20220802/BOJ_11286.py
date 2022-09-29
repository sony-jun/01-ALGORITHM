# heapq 모듈 불러옴
import heapq

numbers = [18, 1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
# heap 빈 리스트 만듬
heap = []

# numbers에 모든 number 순회
for number in numbers:
    # number가 0이 아니면
    if number != 0:
        # heappush 통해서 numbers의 number 넣음
        heapq.heappush(numbers, number)
    else:
        # length가 정수면
        if len(heap):
            print(0)
        else: # 아니면
            # heappop 통해서 빼낸 numbers 출력
            print(heapq.heappop(numbers))