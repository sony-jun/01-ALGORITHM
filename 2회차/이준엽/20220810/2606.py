n = int(input())
m = int(input())
womcom = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    womcom[u].append(v)
    womcom[v].append(u)
wom = 1
visited = []
need_visited = []
need_visited.append(wom)
while need_visited:
    node = need_visited.pop()
    if node not in visited:
        visited.append(node)
        need_visited.extend(womcom[node])
print(len(visited)-1)