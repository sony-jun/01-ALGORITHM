import sys
sys.stdin = open('절대값힙.txt', 'r')

import heapq

heap = [] #비여있는 배열시작
#heapq.heapify(heap)안해도 heapq.heappush(heap,수) 하면 변환됨
N = int(input())

for i in range(N):
    num = int(input())
    if num != 0: #a가 0이 아니면
        heapq.heappush(heap,(abs(num),num)) #리스트에 튜플 형석으로 절대값과, 기존값을 같이 입력
        print(heap)
    elif num == 0: #0이 들어오면 절대값and기존값이 낮은 값을 출력할꺼야
        if len(heap) == 0 : #not heap: #heap이 비여있으면
            print(0)
        else:
            print(heapq.heappop(heap)[1]) #리스트에 0번인덱스값을 가져와서 그값의 1번인덱스값 보여줘