# 촌수계산 
# def dfs(node):
#     for n in matrix[node]:
#         if visited[n] == 0:
#             visited[n] = visited[node]+1
#             dfs(n)
# n = int(input())
# u, v = map(int, input().split())
# m = int(input())
# matrix = [[] for _ in range(n + 1)]
# visited = [0] * (n + 1)
# for _ in range(m):
#     x, y = map(int, input().split())
#     matrix[x].append(y)
#     matrix[y].append(x)
# dfs(u)
# if visited[v] > 0:
#     print(visited[v])
# else:
#     print(-1)  

n = int(input())
u, v = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
stack = [u]
while len(stack) != 0:
    cur = stack.pop()
    for a in matrix[cur]:
        if visited[a] == 0:
            visited[a] = visited[cur] + 1
            stack.append(a)
if visited[v] > 0:
    print(visited[v])
else:
    print(-1)