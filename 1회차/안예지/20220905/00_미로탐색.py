# 2178

from pprint import pprint
from collections import deque

import sys
sys.stdin= open("미로.txt")

# N, M = map(int, input().split())
N, M = 4, 6

# maps = [list(input()) for _ in range(N)]

maps = [['1', '0', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '0', '1', '1']]
# 델타탐색 범위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 방문 리스트 만들기
visited = [[False] * M for _ in range(N)]
# pprint(visited)

# bfs 구현
def bfs():
  # queue 는 deque
  queue = deque([(0,0)])
  r, c = queue.popleft()
  # print(r, c)
    
  while queue:
    cur = 

      
      for idx in range(4):
        nr = dr[idx] + r
        nc = dc[idx] + c
        
    # 델타 탐색 예외 처리
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False:
          queue.append((nr, nc))
          
          
      
    
  
bfs()

