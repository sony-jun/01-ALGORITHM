from collections import deque
import sys

def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:

        v = queue.popleft() # 2차원 리스트의 1번째 1
        print(v, ' v 입니당')
        for i in graph[v]: # graph[1]의 원소 >> [1, 2]
            print(i)
            if not visited[i]: # 1을 방문하지 않았으면, 1을 큐에 넣어주고 방문했으면 넘어감
                queue.append(i) 
                visited[i] = True # 2를 큐에 넣겠네
                print(visited, f'{i} 번째')
            

sys.stdin = open('./2606.txt')

n = int(input())
m = int(input())
graph = [[]]
for i in range(m):
    a, b = map(int, input().split())
    graph.append([a, b])


visited = [False] * (m + 1)
print(graph)
print(visited)
bfs(graph, 1, visited)
print(visited)