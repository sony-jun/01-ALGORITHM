import sys

sys.stdin = open("0_바이러스.txt")

N = int(input())
M = int(input())
list_ = []
visited = [False] * (N + 1)
total = 0

for _ in range(N+1):
    list_.append([])

for i in range(M):
    v1, v2 = map(int, input().split())
    list_[v1].append(v2)
    list_[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for adj in list_[cur]:
            if not visited[adj]:    # True 이면
                visited[adj] = True
                stack.append(adj)

dfs(1)



