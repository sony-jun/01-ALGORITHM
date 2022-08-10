


n,m = map(int,input().split())



graph=[[]for __ in range(n+1)]


visit= [0]*(n+1)


for __ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs (i)-> None:
    visit[i]= True
    stack = [i]
    while stack:
        cur= stack.pop()
        for j in graph[cur]:
            if not visit[j]:
                visit[j]= True
                stack.append(j)
cnt=0
for gr in range(1,len(graph)):
    if not visit[gr]:
        cnt+=1
        dfs(gr)


print(cnt)


