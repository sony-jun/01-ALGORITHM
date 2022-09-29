# 카드1

from collections import deque       # 큐 사용

N = int(input())                    
a = []                              
b = deque(list(range(1, N + 1)))    # 1부터 입력값까지 나열된 큐 생성
while len(b) != 1:                  # 큐 내 데이터가 1개가 되면 멈추는 반복문 작성
    a.append(b.popleft())           # 큐 내 맨 왼쪽 값을 빼서 빈 리스트에 추가.
    b.append(b.popleft())           # 맨 왼쪽 값을 또 빼서 맨 오른쪽에 추가.
print(*a, *b)                       # *를 사용해 개방하여 출력