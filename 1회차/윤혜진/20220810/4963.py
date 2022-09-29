# https://www.acmicpc.net/problem/4963
# 문제4963번.섬의 개수
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
<각 테스트 케이스 마다 아래가 주어짐>
1. 지도의 너비 w, 높이 h
- 0 < w, h <= 50
2. h개의 줄에 지도가 주어짐
- 1: 땅
- 0: 바다
3. 입력의 종료 조건으로 0이 두개 주어짐
'''



# 출력
'''
1. 각 테스트 케이스에 대해서 섬의 개수를 출력
- 가로, 세로, 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형임
- 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 함
'''



# 코드 1 - stack을 이용한 반복문으로 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/4963.txt')

def dfs(node) -> None:
    r, c = node
    graph[r][c] = '0'   # 시작 좌표 방문 체크
    stack = [(r, c)]   # 방문 순서 기록
    while stack:
        r, c = stack.pop()   # 현재 위치하고 있는 좌표

        # 연결되어있는 좌표(땅) 탐색
        # 델타 탐색: 상 하 좌 우 우상향 우하향 좌상향 좌하향
        dr = [-1, 1, 0, 0, -1, 1, -1, 1]
        dc = [0, 0, -1, 1, 1, 1, -1, -1]
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == '1':
                graph[nr][nc] = '0'   # 방문 체크
                stack.append((nr, nc))
                

while True:
    w, h = map(int, input().split())

    # 입력의 종료 조건인지 확인
    if w == 0 and h == 0:
        break

    # 지도 만들기
    graph = [input().split() for _ in range(h)]
    
    # 지도 내 섬의 개수 출력
    cnt = 0   # 땅의 갯수
    for r in range(h):
        for c in range(w):
            # 땅이 있는 곳이면 해당 땅 위치를 시작점으로 두고 깊이우선탐색
            if graph[r][c] == '1':
                dfs((r, c))
                cnt += 1
    print(cnt) 



# 실행결과(메모리:30840KB, 시간:128ms)



# 코드 2 - 재귀를 이용해 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/4963.txt')

sys.setrecursionlimit(10**6)
def dfs(node) -> None:
    # 시작 좌표 방문 체크
    r, c = node
    graph[r][c] = '0'   
    
    # 연결되어있는 좌표(땅) 탐색
    # 델타 탐색: 상 하 좌 우 우상향 우하향 좌상향 좌하향
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == '1':
            dfs((nr, nc))
            

while True:
    w, h = map(int, input().split())

    # 입력의 종료 조건인지 확인
    if w == 0 and h == 0:
        break

    # 지도 만들기
    graph = [input().split() for _ in range(h)]
    
    # 지도 내 섬의 개수 출력
    cnt = 0   # 땅의 갯수
    for r in range(h):
        for c in range(w):
            # 땅이 있는 곳이면 해당 땅 위치를 시작점으로 두고 깊이우선탐색
            if graph[r][c] == '1':
                dfs((r, c))
                cnt += 1
    print(cnt) 



# 실행결과(메모리:33136KB, 시간:112ms)



# 코드 3 - queue를 이용한 반복문으로 bfs 풀이
import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input_text/4963.txt')

def bfs(node) -> None:
    r, c = node
    graph[r][c] = '0'   # 시작 좌표 방문 체크
    q = deque([(r, c)])   # 방문 순서 기록
    while q:
        r, c = q.popleft()   # 현재 위치하고 있는 좌표

        # 연결되어있는 좌표(땅) 탐색
        # 델타 탐색: 상 하 좌 우 우상향 우하향 좌상향 좌하향
        dr = [-1, 1, 0, 0, -1, 1, -1, 1]
        dc = [0, 0, -1, 1, 1, 1, -1, -1]
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == '1':
                graph[nr][nc] = '0'   # 방문 체크
                q.append((nr, nc))
            

while True:
    w, h = map(int, input().split())

    # 입력의 종료 조건인지 확인
    if w == 0 and h == 0:
        break

    # 지도 만들기
    graph = [input().split() for _ in range(h)]
    
    # 지도 내 섬의 개수 출력
    cnt = 0   # 땅의 갯수
    for r in range(h):
        for c in range(w):
            # 땅이 있는 곳이면 해당 땅 위치를 시작점으로 두고 깊이우선탐색
            if graph[r][c] == '1':
                bfs((r, c))
                cnt += 1
    print(cnt) 



# 실행결과(메모리:32468KB, 시간:136ms)