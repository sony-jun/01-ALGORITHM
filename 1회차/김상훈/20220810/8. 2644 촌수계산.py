import sys
from pprint import pprint
sys.setrecursionlimit(10**6)
sys.stdin = open("8. 촌수계산.txt", "r")


# def dfs(v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             res[i] = res[v] + 1
#             dfs(i)
            
n = int(input())
h1 , h2 = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
# res = [0] * (n+1)

for i in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
# if res[h2] > 0:
#     print(res[h2])
# else:
#     print(-1)
        
    
    

pprint(graph)

stack = []
stack.append((h1,0))
visited[h1] = True

while len(stack) != 0:
    number,count = stack.pop()
    
    if number == h2:
        answer = count
        break
    adj_graph = graph[number]
    print(number,adj_graph)
    
    for adj_number in adj_graph:
        if not visited[adj_number]:
            stack.append((adj_number,count+1))
            visited[adj_number] =True
print(answer)

    
