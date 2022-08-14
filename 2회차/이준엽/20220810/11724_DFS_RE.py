import sys
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
relations = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int,input().split())
    relations[u].append(v)
    relations[v].append(u)

visited = [False for i in range(n+1)]
stack = []
cnt = 0

for i in range(1,n+1):
    if visited[i] == False:
        stack.append(i)
        visited[i] = True
        while stack:
            start = stack.pop()
            for j in relations[start]:
                if visited[j] == False:
                    stack.append(j)
                    visited[j] = True
        cnt+=1
print(cnt)