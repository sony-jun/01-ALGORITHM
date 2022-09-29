# 11724.
"""
6 5
1 2
2 5
5 1
3 4
4 6

"""
# N, M = map(int, input().split())
N, M = 6, 5

# 인접리스트 만들기
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# print(graph)

visited = {}
for key in range(1, N + 1):
    visited[key] = False
# print(visited)

def dfs(start):
    answer = 0
    
    stack = [start]
    visited[start] = True

        
    while stack:
        cur = stack.pop()
        
        for adj in graph[cur]:
            if visited[adj] != True:
                visited[adj] = True
                stack.append(adj)
                answer += 1
                
    # 스택이 다 비었을 때 어떻게 다른 시작 정점으로 넘어갈 수 있을까?
    if sum(visited) != len(visited):
        for key in visited:
            if visited[key] == False:
                start = key
                break
    return answer

dfs(1)
    
    
    
    # return 
