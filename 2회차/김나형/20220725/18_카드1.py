import sys

sys.stdin = open("18_카드1.txt")

# N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

from collections import deque
 

list = deque([i for i in range(1, int(input())+1)])
while len(list) > 1:
    print(list.popleft(), end=' ')
    list.append(list.popleft())
print(*list)