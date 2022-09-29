import sys
from pprint import pprint
sys.stdin = open("1_섬의개수.txt", 'r')

while 1:
    dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 12시 방향부터 시계방향으로 탐색
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    w, h = map(int, sys.stdin.readline().split())
    if w + h != 0:
        map_ = []
        nodes = []
        for _ in range(h):
            map_.append([*map(int, sys.stdin.readline().split())])
        
        # 노드 구하는 코드 시작
        
        for y in range(h): # 행 좌표 == 높이 == 좌표평면의 y값
            for x in range(w): # 열 좌표 == 폭 == 좌표평면의 x값
                if map_[y][x] == 1: # 특정 좌표에 섬이 있을 때
                    nodes.append([y, x]) # 현재 좌표가 하나의 섬일때 노드에 그 좌표를 추가
                    for i in range(8): # 몇 번 반복할지 모름
                        ny = y + dy[i] # 일단 값을 갱신하고
                        nx = x + dx[i]
                        while -1 < ny < h and -1 < nx < w: # 만약 그 값이 범위를 벗어나지 않으면
                            if map_[ny][nx] == map_[y][x]: # 또한 만약 이동한 곳의 값이 이동하기 전의 값과 같다면 <<< 이 지점에서 반복하며 끝까지 조회
                                nodes.append([ny, nx]) # 이동한 곳의 좌표도 추가
                                ny = ny + dy[i] # 다음 탐색을 위해 좌표 갱신
                                nx = nx + dx[i]
                            else:
                                break
        
        # 노드 구하는 코드 끝
        
    else:
        break