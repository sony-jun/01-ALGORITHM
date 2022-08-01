# 우유 축제

from collections import deque
T = int(input())
milk = deque(map(int, input().split()))
milk_sequence = [0, 1, 2]
cnt = 0
a = 0
while len(milk) != 0:
    if milk_sequence[a] == milk.popleft():
        cnt += 1
        a += 1
        if a > 2:
            a -= 3
print(cnt)