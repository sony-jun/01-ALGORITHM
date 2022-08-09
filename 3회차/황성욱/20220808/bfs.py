from collections import deque


def bfs(graph, start, visited):

    queue = deque([start]) # 무슨 의미지?  > append(start)
    print(queue)
    visited[start] = True

    while queue:

        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]: # 1차원의 원소
           
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)
