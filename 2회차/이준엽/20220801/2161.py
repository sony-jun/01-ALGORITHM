from collections import deque

n = int(input())

numbers = range(1,n+1)
d_numbers = deque(numbers)
result = []
while len(d_numbers) > 1:
    result.append(d_numbers.popleft())
    d_numbers.append(d_numbers.popleft())
print(*result,d_numbers[0])