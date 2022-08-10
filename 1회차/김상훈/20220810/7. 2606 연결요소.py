import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("7. 연결요소.txt", "r")

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)


# 인접 리스트 공간 , 방문 내역, 연결 요소 변수 생성.
N , M = map(int,input().split()) # 정점, 간선 갯수
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

# 인접 리스트 생성
for _ in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# ---------------------------

# 
for i in range(1, N+1):
    if visited[i] == False:
        result += 1
        dfs(i)
print(graph)       
print(result)
    
            
            
# visited = [False] * (N+1)
# stack = [0]
# visited[0] = True
# cnt = 0
# while stack:
#     cur = stack.pop()
    
#     for adj in graph[cur]:
#         if not visited[adj]:
#             visited[adj] = True 
#             stack.append[adj]
# print(stack)