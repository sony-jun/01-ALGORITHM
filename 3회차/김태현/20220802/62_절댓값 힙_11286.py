import heapq

import sys
sys.stdin = open("62_절댓값 힙_11286.txt", "r")


N = int(input())

hq = []
heapq.heapify(hq)

for i in range(N):
    n = int(input())

    if n == 0: # 입력값이 0이면
        if len(hq) == 0: # 배열이 비어 있으면
            print(0) # 0 출력
        else: # 배열이 비어있지 않으면 # 절댓값이 가장 작은 값 출력 제거
            print(heapq.heappop(hq)[1])  
            # 추가할 때 [abs(n), n] 형태로 입력 했으므로, [1]로 n에 인덱싱 해서 출력 
            # # 어차피 묶여있는 인자는 함께 제거
            
    elif n != 0: # 입력값이 0이 아니면
        heapq.heappush(hq, (abs(n), n)) 
        # 힙에 [abs[n], n]  형태로 추가 
        # 이러면 [0]순으로 정렬 -> [1]순으로 정렬 되므로 절댓값을 기준으로 비교할 수 있음
        # 조건: 절댓값 크기가 같은 것이 여러 개일 경우, n값이 작은 것을 제거 => [0]순 정렬값이 같으면 -> [1]순 정렬값으로 제거