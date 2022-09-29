n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
# False로 초기화 되어있는 리스트
# 방문 처리 리스트
visited = [False] * (n + 1)
total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, c2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [False] * n
def dfs(start):
    # 돌아올때 stack 구현
    # 더 이상 갈 곳이 없을 때 돌아갈 곳
    stack = [start]
    # 처음 시작 방문 처리
    visited[start] = True

    # 더 이상 갈 곳이 없을 때 로직화한 while문
    while stack:
        cur = stack.pop()

        # 예를 들어, 0은 [1, 2]
        # cur에 [1, 2] 대입
        for adj in graph[cur]:
            # 방문해 있지 않았다면 가는 것이다
            if not visited[adj]:
                visited[adj] = True
                # stack에 1 추가
                stack.append(adj)

