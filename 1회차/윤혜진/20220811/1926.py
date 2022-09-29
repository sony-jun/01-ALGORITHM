# https://www.acmicpc.net/problem/1926
# 문제1926번.그림
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 도화지의 세로 크기 n, 가로 크기 m
- 1 <= n, m <= 500
2. (n + 1)개 줄까지 그림의 정보가 주어짐
- 0: 색칠이 안된 부분
- 1: 색칠이 된 부분
'''



# 출력
'''
1. 그림의 개수
- 가로, 세로로 연결된 것만 연결된 것
2. 그 중 가장 넓은 그림의 넓이를 출력
- 단 그림이 하나도 없는 경우, 가장 넓은 그림의 넓이는 0
'''



# 코드 1 - stack을 이용한 반복문으로 dfs 구현
import sys
from pprint import pprint

sys.stdin = open('input_text/1926.txt')

def dfs(start_r, start_c):
    graph[start_r][start_c] = 0   # 시작 위치 방문 체크
    stack = [(start_r, start_c)]   # 이동가능한 그림 위치
    pic_size = 1   # 그림 넓이

    while stack:
        r, c = stack.pop()   # 현재 위치

        # 현재 위치에서 델타 탐색
        dr = [0, 0, 1, -1]   # 동서남북
        dc = [1, -1, 0, 0]
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == 1:
                graph[nr][nc] = 0   # 방문 처리
                stack.append((nr, nc))
                pic_size += 1
    
    return pic_size
            

# 도화지 그래프 만들기
n, m = map(int, input().split())   # n: 세로 크기, m: 가로크기
graph = [list(map(int, input().split())) for _ in range(n)]

# 그림 갯수 카운팅
cnt = 0
biggest_pic = 0   # 가장 큰 그림의 넓이
for r in range(n):
    for c in range(m):
        # 현재 위치가 그림이면, 깊이우선탐색
        if graph[r][c] == 1:
            biggest_pic = max(biggest_pic, dfs(r, c))
            cnt += 1
print(cnt)
print(biggest_pic)



# 실행결과(메모리:44424KB, 시간:684ms)



# 코드 2 - 재귀를 이용해 dfs 구현
import sys
from pprint import pprint

sys.stdin = open('input_text/1926.txt')

sys.setrecursionlimit(10**6)
def dfs(r, c) -> None:
    global pic_size

    graph[r][c] = 0   # 방문 처리
    
    # 그림 넓이 1 증가
    pic_size += 1

    # 현재 위치에서 델타 탐색
    dr = [0, 0, 1, -1]   # 동서남북
    dc = [1, -1, 0, 0]
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == 1:
            dfs(nr, nc)
            

# 도화지 그래프 만들기
n, m = map(int, input().split())   # n: 세로 크기, m: 가로크기
graph = [list(map(int, input().split())) for _ in range(n)]

# 그림 갯수 카운팅
cnt = 0
biggest_pic = 0   # 가장 큰 그림의 넓이
for r in range(n):
    for c in range(m):
        # 현재 위치가 그림이면, 깊이우선탐색
        if graph[r][c] == 1:
            pic_size = 0
            dfs(r, c)
            cnt += 1
            biggest_pic = max(biggest_pic, pic_size)
print(cnt)
print(biggest_pic)



# 실행결과(실패:메모리 초과)



# 코드 3 - 큐를 이용한 반복문으로 bfs 구현
import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input_text/1926.txt')

def bfs(start_r, start_c):
    graph[start_r][start_c] = 0   # 시작 위치 방문 체크
    q = deque([(start_r, start_c)])   # 이동가능한 그림 위치
    pic_size = 1   # 그림 넓이

    while q:
        r, c = q.popleft()   # 현재 위치

        # 현재 위치에서 델타 탐색
        dr = [0, 0, 1, -1]   # 동서남북
        dc = [1, -1, 0, 0]
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == 1:
                graph[nr][nc] = 0   # 방문 처리
                q.append((nr, nc))
                pic_size += 1
    
    return pic_size
            

# 도화지 그래프 만들기
n, m = map(int, input().split())   # n: 세로 크기, m: 가로크기
graph = [list(map(int, input().split())) for _ in range(n)]

# 그림 갯수 카운팅
cnt = 0
biggest_pic = 0   # 가장 큰 그림의 넓이
for r in range(n):
    for c in range(m):
        # 현재 위치가 그림이면, 깊이우선탐색
        if graph[r][c] == 1:
            biggest_pic = max(biggest_pic, bfs(r, c))
            cnt += 1
print(cnt)
print(biggest_pic)



# 실행결과(메모리:32460KB, 시간:720ms)