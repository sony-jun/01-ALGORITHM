import sys
sys.stdin = open("9. 바이러스.txt", "r")

n = int(input()) # 정점(노드) 갯수
m = int(input()) # 간선 갯수 
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
visited = [False] * (n+1)
stack = [1]
visited[0] = True
cnt = -1   #맨 처음 시작 노드를 카운트에서 제외하기 위해 -1로 시작  
while stack:
    cur = stack.pop()
        
    for adj in graph[cur]:
        if visited[adj] == False:
            visited[adj] = True
            stack.append(adj)
            cnt += 1
print(cnt)