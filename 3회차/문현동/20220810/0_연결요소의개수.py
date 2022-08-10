import sys
from pprint import pprint
sys.stdin = open("0_연결요소의개수.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
adjacent_list = []
edges = []
cnt = 0

for _ in range(N + 1):
    adjacent_list.append([])

for _ in range(M):
    edges.append([*map(int, sys.stdin.readline().split())])

for i in edges:
    adjacent_list[i[0]].append(i[1])
    adjacent_list[i[1]].append(i[0])

# 닫힌 루프의 탐색이 끝날때마다 cnt += 1

visited = [0] * (N + 1)
stack = []

for j in range(1, N + 1): # 1 ~ 6
    
    stack += (adjacent_list[j]) # [2, 5]
    if visited[j] == 1:
        pass
    else:
        cnt += 1
        while stack:
            
            current = stack.pop(0) # [2, 5] -> 2, [5]
                
            for adj in adjacent_list[current]: # [1, 5] -> 1, [5]
                if not visited[adj]: # visited[1]
                    visited[adj] = 1 # visited[1] = 1
                    stack.append(adj) # [1, 5]

print(cnt)