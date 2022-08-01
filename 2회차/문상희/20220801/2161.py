from collections import deque

number = int(input())

queue = list(range(1, number + 1))

while len(queue) > 1:
    print(queue.pop(0), end = ' ')
    # queue에서 0의 위치에 있는 값을 제거하며 출력
    queue.append(queue.pop(0))
    # queue에서 0의 위치에 있는 값을 제거하고 맨 뒤에 추가
print(queue[0])
# 마지막 남은 queue의 값을 출력