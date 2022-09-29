# https://www.acmicpc.net/problem/2606
import sys
sys.stdin = open('B2606.txt')

V = int(input())
E = int(input())
network = [[] * (V+1) for _ in range(V+1)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    network[v1].append(v2)
    network[v2].append(v1)
# print(network)

cnt = 0 
# stack = [start] #?
visited = [False] * V+1

def dfs(stard):
while stack:
     current = stack.pop()
     
     for adj in network[adj]: #정점 돌면서 
         if not visited[adj]: # 어 ? 여기 안갔네 ? 
             visited[adj] = True # 가서 갔다고 표시 
             stack.append(adj)
          
        # 감염된 수 ? = visited 수 
        #print(sum(visited) -1) 하면 됨 왜 ? True는 1이니까
        # -1하는 이유는 시작노드 뺄려고
        