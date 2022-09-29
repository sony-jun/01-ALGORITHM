# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6

N = int(input())
A, B = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

visit = []

result = [0]*N
def dfs(v, num):
    num += 1
    visit[v] = 1

    if v == B:
        result.append(num)

    for i in graph[v]:
        if not visit[i]:
            dfs(i, num)
          
dfs(A, 0)

if len(result) == 0:
    print(-1)

else:
    print(result,visit)
    print(result[0] - 1)