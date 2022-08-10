# https://www.acmicpc.net/problem/11724
# 문제11724번.연결 요소의 개수
# 시간제한:3초, 메모리제한:512MB



# 입력
'''
<무방향 그래프>
1. 정점 개수 N, 간선 개수 M
- 1 <= N <= 1,000
- 0 <= M <= N x (N -1)/2
2. M개의 줄에 간선의 양 끝점(정점) u, v
- 1 <= u, v <= N
'''



# 출력
'''
1. 연결 요소의 개수 출력
'''



# 코드 1 - stack을 이용한 반복문으로 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/11724.txt')

# 현재 노드와 연결된 모든 노드를 방문 체크하는 함수
def dfs(node) -> None:   
    visited[node] = True   # 시작 노드 방문 체크
    stack = [node]   # 방문(탐색) 기록
    while stack:
        now = stack.pop()   # 현재 위치하고 있는 노드

        for n in graph[now]:   # 인접 노드 탐색
            if not visited[n]:
                visited[n] = True   # 방문(탐색) 체크
                stack.append(n)   # 방문(탐색) 기록    


# 인접 리스트 만들기
N, M = map(int, input().split())   # N: 노드의 개수, M: 간선의 개수
graph = [[] for _ in range(N + 1)]   # 인덱스: 노드 1 ~ 노드 N
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 연결요소 개수 출력
visited = [False] * (N + 1)
cnt = 0
for node in range(1, N + 1):
    # 아직 방문하지 않은 곳이면, 해당 노드를 시작노드로 두고 깊이우선탐색
    if not visited[node]:
        dfs(node)
        cnt += 1

print(cnt)



# 실행결과(메모리:64368KB, 시간:828ms)



# 코드 2 - 재귀를 이용해 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/11724.txt')

# 현재 노드와 연결된 모든 노드를 방문 체크하는 함수
sys.setrecursionlimit(10**6)
def dfs(node) -> None:   
    # 방문 체크
    visited[node] = True   

    # 인접 노드 탐색
    for n in graph[node]:   
        if not visited[n]:
            dfs(n)


# 인접 리스트 만들기
N, M = map(int, input().split())   # N: 노드의 개수, M: 간선의 개수
graph = [[] for _ in range(N + 1)]   # 인덱스: 노드 1 ~ 노드 N
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 연결요소 개수 출력
visited = [False] * (N + 1)
cnt = 0
for node in range(1, N + 1):
    # 아직 방문하지 않은 곳이면, 해당 노드를 시작노드로 두고 깊이우선탐색
    if not visited[node]:
        dfs(node)
        cnt += 1

print(cnt)



# 실행결과(메모리:64840KB, 시간:800ms)



# 코드 3 - queue를 이용한 반복문으로 bfs 풀이
import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input_text/11724.txt')

# 현재 노드와 연결된 모든 노드를 방문 체크하는 함수
def bfs(node) -> None:   
    visited[node] = True   # 시작 노드 방문 체크
    q = deque([node])   # 방문(탐색) 기록
    while q:
        now = q.popleft()   # 현재 위치하고 있는 노드

        for n in graph[now]:   # 인접 노드 탐색
            if not visited[n]:
                visited[n] = True   # 방문(탐색) 체크
                q.append(n)   # 방문(탐색) 기록    


# 인접 리스트 만들기
N, M = map(int, input().split())   # N: 노드의 개수, M: 간선의 개수
graph = [[] for _ in range(N + 1)]   # 인덱스: 노드 1 ~ 노드 N
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 연결요소 개수 출력
visited = [False] * (N + 1)
cnt = 0
for node in range(1, N + 1):
    # 아직 방문하지 않은 곳이면, 해당 노드를 시작노드로 두고 깊이우선탐색
    if not visited[node]:
        bfs(node)
        cnt += 1

print(cnt)



# 실행결과(메모리:64512KB, 시간:856ms)