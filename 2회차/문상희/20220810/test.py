# # dfs 구현 예

# visited = [0] * N                   # 방문 처리 리스트 만들기

# def dfs(start):                     # 돌아갈 곳을 기록
#     stack = [start]                 # 싲작 정점 방문 처리
#     visited[start] = True

#     while stack:                    # 스택이 빌 때까지(돌아갈 곳이 없을 때까지) 반복
#         cur = stack.pop()           # 현재 방문 정점(후입선출)

#         for adj in gragh[cur]:      # 인접한 모든 정점에 대해
#             if not visited[adj]:    # 아직 방문하지 않았다면
#                 visited[adj] = True # 방문 처리
#                 stack.append(adj)   # 스택에 넣기

# dfs(0)

