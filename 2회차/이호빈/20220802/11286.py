import heapq
import sys 

input = sys.stdin.readline
# 빈리스트 만들기
heap = []

#연산의 개수
for _ in range(int(input())):
    #입력값 받기
    number = int(input())
    # 입력값이 0이 아니라면 값을 추가
    if number != 0:
        #number 절댓값도 넣는다
        heapq.heappush(heap, (abs(number), number))
    else:
        # heap에 아무것도 없다면
        if len(heap) == 0:
            print(0)
        # len(heap) != 0 heappop한 것을 출력, 입력값을 출력되게 하게끔
        else:
            print(heapq.heappop(heap)[1])
        


