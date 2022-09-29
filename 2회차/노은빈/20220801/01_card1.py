#큐를 이용한 풀이
#큐 : 가장 먼저 들어온 데이터가 가장 먼저 나감
n = int(input())  
queue = list(range(1, n+1))  #queue를 리스트로 만듦

while len(queue) > 1:  #queue의 길이가 1보다 크다면 ->1이 될 때까지 반복
    print(queue.pop(0), end=' ')  #0 위치의 값 print하고 공백
    queue.append(queue.pop(0))  #0 위치에 있는 값 삽입(맨 뒤로 감)

print(queue[0]) #마지막에 남은 카드 출력


#덱을 이용한 풀이
#덱 : 양방향 삽입, 추출 가능
from collections import deque

n = int(input())  
queue = deque(range(1, n+1))  #queue를 덱으로 만듦

while len(queue) > 1:
    print(queue.popleft(), end=' ')  #맨 왼쪽의 값 print하고 공백
    queue.append(queue.popleft())  #맨 왼쪽 위치에 있는 값 삽입(맨 뒤로 감)

print(queue[0]) #마지막에 남은 카드 출력