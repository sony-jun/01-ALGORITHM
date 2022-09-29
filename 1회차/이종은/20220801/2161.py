from collections import deque

n = int(input()) # 예제 7입력 
queue = deque(range(1, n+1)) # 1~7 반복

while len(queue)>1 : # 숫자리스트가 1개 이상일때 반복
    print(queue.popleft(), end=" ") # 맨 왼쪽 숫자(뺀 숫자) 출력
    queue.append(queue.popleft()) # 맨 왼쪽 숫자 빼고 그 숫자를 오른쪽에 다시 추가하기 

print(queue[0]) # 큐 리스의 첫번째 인덱스 값 출력 = 남게 되는 카드 번호