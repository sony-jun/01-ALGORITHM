n = 7

graph = []
for _ in range(n+1): # n+1인 이유는??
    graph.append([])

visited = [False]*(n+1) # 방문 처리 리스트 만들기

def dfs(start):
    stack = [start] # 처음 시작 숫자이며, 돌아갈 곳을 기록하기 위해 스택에 넣어줌
    visited[start] = True # 시작 정점 방문 기록 
    
    while stack: #스택이 빌 때까지, 돌아갈 곳이 없을때까지 반복
        cur = stack.pop() # 현재 방문 정점(후입선출: 최근에 들어온 것 부터 먼저 나감)
        
        for i in graph[cur]:# 인접한 모든 정점에 대해
            if not visited[i] : # 아직 방문하지 않았다면
                 visited[i] = True # 방문 처리 
                 stack.append(i) # 스택에 넣기

dfs(1)