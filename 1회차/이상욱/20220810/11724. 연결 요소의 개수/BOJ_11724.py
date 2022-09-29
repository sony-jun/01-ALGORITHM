import sys
sys.stdin = open('11724.txt')

N, M = map(int, input().split())
con = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for i in range(M):
    v1, v2 = map(int, input().split())
    con[v1].append(v2)
    con[v2].append(v1)

count = 0

for j in range(1, N+1):
    if not visited[j]:
        count += 1
        stack = [j]
        visited[j] = True
        
        while stack:
            cur = stack.pop()
        
            for adj in con[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)
            
print(count)