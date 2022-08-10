import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

num = set(range(n+1))
linum = list(range(n+1))
cnt=0
while num:
    visit = []
    need_visit = []
    need_visit.append(linum.pop())
    while need_visit:
        node = need_visit.pop()
        if node not in visit:
            visit.append(node)
            need_visit.extend(graph[node])
    if visit and num != num-set(visit):        
        num = num-set(visit)
        cnt+=1
print(cnt-1)