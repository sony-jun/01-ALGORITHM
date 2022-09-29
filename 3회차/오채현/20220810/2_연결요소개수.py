n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
vst = [False] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt = 0


def dfs(st):
    stk = [st]
    vst[st] = True

    while stk:
        cur = stk.pop()

        for adj in graph[cur]:
            if not vst[adj]:
                vst[adj] = True
                stk.append(adj)


for i in range(1, n + 1):
    if not vst[i]:
        dfs(i)
        cnt += 1

print(cnt)
