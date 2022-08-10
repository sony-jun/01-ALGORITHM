# https://www.acmicpc.net/problem/2644
# 문제2644번.촌수 계산
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 전체 사람의 수 n
2. 촌수를 계산해야하는 서로 다른 두 사람의 번호
3. 부모 자식들 간의 관계의 개수 m
4. 부모 자식간의 관계(간선)를 나타내는 두 번호 x, y
- 사람들은 연속된 번호로 표시됨(1 <= n <= 100)
- 번호 x: 번호 y의 부모 번호를 나타냄 
- x: 부모
- y: 자식
'''



# 출력
'''
1. 두 사람의 촌수를 출력
- 친척관계가 전혀 없어 촌수를 계산할 수 없을 때는 -1을 출력
'''



# 코드 1 - stack을 이용한 반복문으로 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/2644.txt')

# 노드1과 노드2의 촌수 
# = 시작 노드(노드1)에서 목적지 노드(노드2)까지 가는데 지나는 간선 수
def dfs(start, end) -> int:
    visited[start] = 1   # 시작 노드 방문 체크
    stack = [start]   # 방문 순서 기록
    while stack:
        now = stack.pop()   # 현재 위치하고 있는 노드

        # 현재 위치하는 노드가 목적지 노드인 경우
        if now == end:
            return visited[now] - 1
        
        # 인접 노드 탐색
        for n in graph[now]:
            if not visited[n]:
                visited[n] = visited[now] + 1   # 방문 체크
                stack.append(n)   # 방문 순서 기록

    return -1


n = int(input())   # 전체 사람의 수 = 정점 수
p1, p2 = map(int, input().split())   # 나중에 p1과 p2의 촌수를 파악해 출력해야함

# 무방향 그래프의 인접 리스트 만들기
graph = [[] for _ in range(n + 1)]
edge_cnt = int(input())   # 부모 자식들 간의 관계 수 = 간선 수
for _ in range(edge_cnt):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

# p1과 p2의 촌수 출력
visited = [0] * (n + 1)
print(dfs(p1, p2))



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 2 - 재귀를 이용해 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/2644.txt')

# 노드1과 노드2의 촌수 
# = 시작 노드(노드1)에서 목적지 노드(노드2)까지 가는데 지나는 간선 수
def dfs(node1, node2, cnt) -> None:
    visited[node1] = cnt   # 방문 체크
    
    # 현재 위치하는 노드가 목적지 노드인 경우
    if node1 == node2:
        return 
    
    # 인접 노드 탐색
    for n in graph[node1]:
        if not visited[n]:
            dfs(n, node2, cnt + 1)
    return 


n = int(input())   # 전체 사람의 수 = 정점 수
p1, p2 = map(int, input().split())   # 나중에 p1과 p2의 촌수를 파악해 출력해야함

# 무방향 그래프의 인접 리스트 만들기
graph = [[] for _ in range(n + 1)]
edge_cnt = int(input())   # 부모 자식들 간의 관계 수 = 간선 수
for _ in range(edge_cnt):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

# p1과 p2의 촌수 출력
visited = [0] * (n + 1)
dfs(p1, p2, 1)
print(visited[p2] - 1 if visited[p2] else -1)



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 3 - 큐를 이용한 반복문으로 bfs 풀이
import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input_text/2644.txt')

# 노드1과 노드2의 촌수 
# = 시작 노드(노드1)에서 목적지 노드(노드2)까지 가는데 지나는 간선 수
def bfs(start, end) -> None:
    visited[start] = 1   # 시작 노드 방문 체크
    q = deque([start])   # 방문 순서 기록
    while q:
        now = q.popleft()   # 현재 위치하고 있는 노드

        # 현재 위치하는 노드가 목적지 노드인 경우
        if now == end:
            return visited[now] - 1
        
        # 인접 노드 탐색
        for n in graph[now]:
            if not visited[n]:
                visited[n] = visited[now] + 1   # 방문 체크
                q.append(n)   # 방문 순서 기록

    return -1


n = int(input())   # 전체 사람의 수 = 정점 수
p1, p2 = map(int, input().split())   # 나중에 p1과 p2의 촌수를 파악해 출력해야함

# 무방향 그래프의 인접 리스트 만들기
graph = [[] for _ in range(n + 1)]
edge_cnt = int(input())   # 부모 자식들 간의 관계 수 = 간선 수
for _ in range(edge_cnt):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

# p1과 p2의 촌수 출력
visited = [0] * (n + 1)
print(bfs(p1, p2))



# 실행결과(메모리:32460KB, 시간:92ms)