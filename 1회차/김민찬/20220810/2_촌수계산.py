import sys

sys.stdin = open("2_촌수계산.txt")

n = int(input()) # 전체 사람의 수 = n
a, b = map(int, input().split()) # 서로 다른 두 사람의 번호 = a, b
m = int(input()) # 부모 자식들간의 관계의 개수 = m
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(v): # dfs 이용해서 푸는 문제
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

dfs(a)
if res[b] > 0:
    print(res[b])
else:
    print(-1)