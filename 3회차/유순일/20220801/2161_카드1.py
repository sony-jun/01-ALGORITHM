from collections import deque

numbers = [1, 2, 3, 4, 5]

queue = deque(numbers)

queue.append(6)

queue.popleft()

print(queue)

# #2
# n = int(input())
# queue = deque(range(1, n + 1))

# while len(queue) > 1:
#     print(queue.popleft(), end = " ")
#     queue.append(queue.popleft())
    
# print(queue[0])

# n = int(input())
# queue = list(range(1, n + 1))

# while len(queue) > 1:
#     print(queue.pop(0), end = ' ')
#     queue.append(queue.pop(0))
    
# print(queue[0])