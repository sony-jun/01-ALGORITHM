n = int(input())
m = int(input())


visit=[0]*(n+1)

coms= [[] for __ in range(n+1)]


for __ in range(m):
    u,v = map(int,input().split())
    coms[u].append(v)
    coms[v].append(u)

def virus(i):
    stack=[i]
    visit[i]=1
    st = stack.pop()
    for j in coms[st]:
        if visit[j]==0:
            visit[j]=1
            virus(j)

virus(1)

print(sum(visit)-1)



