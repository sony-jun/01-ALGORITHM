from collections import deque

N = int(input()) # 숫자 입력
#큐 생성 1부터 N까지
queue = deque(range(1,N+1)) 
result = [] # 빈 리스트(A)
while len(queue)!=1: # 큐가 길이가 1보다 크면
    result.append(queue[0]) # A에 큐 하나 추가
    queue.popleft() # 추가한 수 제거
    queue.append(queue[0]) # 큐 맨 앞수 복붙
    queue.popleft() # 이동한 수 제거 >>반복
#큐의 마지막 한수 추가
result.append(int(queue[0])) 
#출
for i in result:
    print(i, end= " ")