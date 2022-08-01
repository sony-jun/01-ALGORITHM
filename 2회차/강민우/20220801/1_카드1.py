from collections import deque

N = int(input())

number = deque(range(1, N+1))

while len(number) > 1:
    print(number.popleft(), end = ' ')
    number.append(number.popleft())

