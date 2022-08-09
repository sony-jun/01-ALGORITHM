from collections import deque

def bfs(n, m):
    queue = deque()
    queue.append(n)
    MAX = 10001
    arr = [0] * MAX
    while queue:

        v = queue.popleft()
        
        if v == m:
            return arr[v]

        dx = [v - 1, v + 1, 2*v]
        for d in dx:
            if 0 <= d < MAX and not arr[d]:
                arr[d] = arr[v] + 1
                queue.append(d)   

n, m = map(int, input().split())
print(bfs(n, m))