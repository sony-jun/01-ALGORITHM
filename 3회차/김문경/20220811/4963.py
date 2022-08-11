import sys
from pprint import pprint
sys.stdin = open('test.txt')

# 너비와 높이
# w, h = map(int, input().split())
w, h = 5 ,4

# 지도 입력 받기
island = []
for i in range(h):
    island.append(list(map(int, input().split())))

# 방문 리스트 만들기
visited = [[0] * w for _ in range(h)]
pprint(visited, width = 40)

# 델타는 8방향
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]

# 8방향 움직일 때 전부 0이면 카운트 종료
cnt = 0
for x in range(h):
    for y in range(w):
        for d in directions:
            # x, y가 0,0 부터 탐색 시작
            # 일단 위치가 바다든 섬이든 탐색했기때문에 1로 두자
            visited[x][y] == 1
            # 항상 기준점에서 1인지 0인지 알고 시작, 0이면 의미없음
            if island[x][y] == 0:
                continue
            # 델타 이동한 좌표가 범위 안에 들어올때만 고려
            newx = x + directions[d][0]
            newy = y + directions[d][1]
            if not (-1 < newx < h and -1 < newy < w):
                continue
            
            

