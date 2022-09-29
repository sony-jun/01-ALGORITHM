import sys
import heapq
input = sys.stdin.readline

t = int(input())
list_heap = []

for _ in range(t):
    num = int(input())
    if num == 0: #입력한 값이 0인경우
        if list_heap: #절대값이 작은 값을 뽑아내 출력시킨다.
            print(heapq.heappop(list_heap)[1])
        else: #힙이 비어있는 경우 0을 출력시킨다.
            print(0) 
    else:
        #입력한 값이 0이 아닌 경우 입력한 숫자와 절대값을 추가한다.
        #abs 함수는 안의 값을 절대값으로 바꿔주는 함수다.
        heapq.heappush(list_heap, (abs(num), num))