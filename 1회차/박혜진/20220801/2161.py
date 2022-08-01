# 입력한 숫자 N번째까지 순서대로 숫자 리스트를 만든다
a = int(input())
num = list(range(1, a + 1))

# 큐로 푸는 방법
# 리스트 안에 숫자가 1개가 되면 반복을 멈춘다.
while len(num) > 1 :
  # 리스트의 가장 앞의 숫자를 버리고, 버린 숫자를 출력한다.
  print(num.pop(0), end=' ')
  # 리스트의 가장 앞의 숫자를 버림과 동시에 맨 뒤에 추가한다.
  num.append(num.pop(0))
# 리스트 안의 숫자가 1개가 남으면 그 숫자를 마지막으로 출력한다.
print(num[0])

# 덱으로 푸는 방법
from collections import deque

b = int(input())

deq = deque(range(1, b + 1))

while len(deq) > 1 :
  # 덱은 왼쪽과 오른쪽을 구분할 수 있다.
  # 왼쪽 삭제/삽입 : popleft() / appendleft()
  # 오른쪽 삭제/삽입 : pop() / append()
  print(deq.popleft(), end=' ')
  deq.append(deq.popleft())

print(deq[0])