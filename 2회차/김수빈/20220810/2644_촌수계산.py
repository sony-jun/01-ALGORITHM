n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)

stack = []
stack.append((start, 0)) # 촌수 시작 0
visited[start] = 1

while stack:
    # 촌수 cnt
    number, cnt = stack.pop()
    if number == end:
        answer = cnt
        break
    for adj in graph[number]:
        if not visited[adj]:
            visited[adj] = 1
            stack.append(adj, cnt + 1)

print(answer)