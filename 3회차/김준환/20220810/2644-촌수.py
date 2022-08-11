import sys
input = sys.stdin.readline

# 비어있는 인접 행렬, 방문 체크 리스트 만들기
n = int(input())
start, end = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

# 인접 행렬 완성
for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# dfs 함수 활용
def Dfs(start):
    stack = [start]
    visited[start] = 0
    cnt = 1

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if adj == end:
                cnt += 1
                visited[adj] += cnt
                return
            if visited[adj] == -1:
                visited[adj] += cnt
                stack.append(adj)
                if adj == graph[cur][-1]:
                    cnt += 1
        
Dfs(start)
print(visited[end])