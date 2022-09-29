import sys
input = sys.stdin.readline

def dfs(person, degree):
    degree += 1
    visited[person] = 1

    if person == person2:
        ans.append(degree)
    
    for i in graph[person]:
        if not visited[i]:
            dfs(i, degree)


n = int(input())
person1, person2 = map(int, input().split())
m = int(input())
ans = []
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(person1, 0)

if ans:
    print(ans[0]-1)
else:
    print(-1)