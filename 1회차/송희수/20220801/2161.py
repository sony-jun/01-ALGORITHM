from collections import deque

import sys

sys.stdin = open("2161.txt")


# queue = list(range(1,n+1))

# while len(queue) > 1:
#     print(queue.pop(0), end = " ")
#     queue.append(queue.pop(0))

# print(queue[0])
def solve(n):
    queue = deque([x for x in range(1, n+1)])
    cnt = 1
    result = []

    while queue:
        if cnt % 2 == 1:
            x = queue.popleft()
            result.append(x)
        else:
            x = queue.popleft()
            queue.append(x)
        cnt += 1

    return result

if __name__ == '__main__':
    n = int(input())

    print(*solve(n)) 
    