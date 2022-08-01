# N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.
# 큐

from collections import deque

# N = int(input())
N = 7
que_list = []

for i in range(1,N+1):
    que_list.append(i)
    que = deque(que_list)
while len(que)!=1:
    que.popleft()
    que.append(que.popleft())
print(que)