n = int(input()) # 사람 수
s,e = map(int,input().split()) # 촌수 구해야하는 사람들
edge = int(input()) # 부모자식관계 갯수. 간선 수?
graph_list = [[] for _ in range(n+1)]

for _ in range(edge):
    u,v = map(int,input().split()) # parents, child
    graph_list[u].append(v)
    graph_list[v].append(u)    

print(graph_list) 

visited = [False]* (n+1) # node를 읽을때마다 visited reset
result = [0] *(n+1) # start node에서 index n번째 노드를 방분하는 횟수를 리스트로 가진 result

def dfs(s):
    visited[s] = True
    print(visited)
    for i in graph_list[s]: 
        if not visited[i]: # visited[i] == False?
            print(result)
            result[i] = result[s] + 1
            dfs(i)

dfs(s)
if result[e]>0:
    print(result[e])
else: print(-1)