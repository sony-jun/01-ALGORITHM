n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1) 

# 촌수 리스트를 따로 만들어서 모든사람의 촌수가 들어간다.
chon = [-1] * (n+1)  

def dfs(start):
    stack = [start]
    chon[start] = 0
    while stack:
        v = stack.pop()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                chon[w] = chon[v] + 1
                stack.append(w)
dfs(A)
print(chon[B])
