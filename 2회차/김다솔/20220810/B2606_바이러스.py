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
# print(network) 인접리스트

# cnt = 0 
# 1번 컴퓨터 시작 정점
visited = [False] * V

def dfs(start): #dfs(1) 하면 1번정점부터 시작 
    stack = [start] #젤 먼저 간 곳 = 돌아갈 곳 
    visited[start] = True #갔다왔다고 표시 
    while stack: # 빌 때까지 반복 
        current = stack.pop() #지금 정점 1에서 시작했으니까 처음은 1
        #-for문 다 돌고 지금 자리 갓네? 빼고 또 갔네? 빼고 다빠지면 0이라 while문 종료
        for adj in network[current]: #network[1] 요소순회=인접정점 다 방문
            if not visited[adj]: #visited[2]어 ? 여기 안갔네 ? 
                visited[adj] = True # 2가서 갔다고 표시 
                stack.append(adj) 
        return visited

print(sum(dfs(1))-1) 
# 1번 정점에서 시작
# 감염된 수 ? = visited 수 
#print(sum(visited) -1) 하면 됨 왜 ? True는 1이니까
# -1하는 이유는 시작노드 뺄려고
        