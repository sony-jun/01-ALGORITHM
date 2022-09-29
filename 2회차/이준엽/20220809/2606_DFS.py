# cnt=0
# def DFS(virus):
#     global cnt
#     visited[virus]=1

#     for i in network[virus]:
#         if (visited[i]==0):
#             DFS(i)
#             cnt+=1

# def BFS(virus):
#     global cnt
#     visited[virus] = 1
#     queue = [virus]
#     while queue:
#         for i in network[queue.pop()]:
#             if (visited[i]==0):
#                 visited[i]=1
#                 queue.insert(0, i)
#                 cnt+=1
# ################MAIN###############
# N= int(input())
# link = int(input())

# network = [[]*(N+1) for _ in range(N+1)]

# for i in range(link):
#     a, b = map(int, input().split())
#     network[a].append(b)
#     network[b].append(a)

# visited = [0]*(N+1)
# BFS(1)
# #DFS(1)
# print(cnt)


# number = int(input())
# m = int(input())
# graph = [[] for i in range(number+1)]
# for i in range(m):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# visited = []
# def dfs_recursive(graph, start):
# ## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
#     visited.append(start)
 
#     for node in graph[start]:
#         if node not in visited:
#             dfs_recursive(graph, node)
#     return visited

# dfs_recursive(graph, 1)
# print(visited)

# n = int(input())
# m = int(input())
# graph = [[] for i in range(n+1)]
# for i in range(m):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# visited = []
# wom = 1
# visited.append(wom)
# def dfs(wom):
#     for w in graph[wom]:
#         if w not in visited:
#             visited.append(w)
#             dfs(w)
# dfs(1)
# print(len(visited)-1)


n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
need_visited = []
visited = []
need_visited.append(1)
while need_visited:
    node = need_visited.pop()
    if node not in visited:
        visited.append(node)
        need_visited.extend(graph[node])
print(len(visited)-1)