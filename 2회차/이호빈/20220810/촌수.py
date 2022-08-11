# from collections import deque
# #n은 노드의 개수
# n = int(input())
# #관계를 입력으로 받아주고
# r1, r2 = map(int, input().split())
# m = int(input())
# #그래프를 만들어 주고
# graph = [[] * (n + 1) for _ in range(n + 1)]
# # 인접 리스트를 만들고
# for _ in range(m):
#     c1, c2 = map(int, input().split())
#     graph[c1].append(c2)
#     graph[c2].append(c1)

# #결과값을 담아줄 변수 
# cnt = 0
# #거리 계산을 위한 변수 
# visited = [0] * (n + 1)

# def bfs(start):
#     #큐를 구현하기 위해 deque라이브러리 사용
#     queue = deque([start])

#     #큐가 빌 때까지 반복
#     while queue:
#         #큐에서 하나의 원소를 뽑는다
#         v = queue.popleft()
#         for i in graph[v]:
            
                