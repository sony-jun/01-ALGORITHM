from collections import deque

n = int(input())
m = int(input())

matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

i = 1
cnt = 0
virus = deque()
virus.append(i)
check = [1]

while virus:
    i = virus.popleft()

    for j in range(n + 1):
        if matrix[i][j] == 1:
            if j not in check:
                virus.append(j)
                check.append(j)
                cnt += 1

print(cnt)
