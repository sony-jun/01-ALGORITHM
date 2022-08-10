import sys
input = sys.stdin.readline

# dfs 탐색
def dfs(v):
    for i in graph[v]:
        if visited[i] == -1:
            # 자식노드 = 부모노드가 갖는 촌수 + 1
            visited[i] = visited[v] + 1
            dfs(i)

n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
# 관계 없다면 -1을 출력할 수 있도록 -1로 초기화
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[A] = 0
# A가 시작노드
dfs(A)
# 도착노드와 시작노드와의 거리 출력
print(visited[B])