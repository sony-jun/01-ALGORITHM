# https://www.acmicpc.net/problem/2178
# 문제2178번.미로 탐색
# 시간제한:1초, 메모리제한:192MB



# 입력
'''
1. 두 정수 N, M
- N x M 크기의 배열로 표현되는 미로
- 2 <= N, M <= 100
2. N개의 줄에 M개의 정수가 붙어서 주어짐
'''



# 출력
'''
1. 지나야하는 최소의 칸 수 출력
- 1: 이동할 수 있는 칸
- 0: 이동할 수 없는 칸
- (1,1)에서 출발하여 (N,M)의 위치로 도착
'''



# 코드
import sys
from collections import deque

sys.stdin = open('input_text/2178.txt')

# 미로 탈출
def escape_maze(maze, N, M):   # N: 행 크기, M: 열 크기
    q = deque([(0, 0)])   # 이동가능한 좌표
    while q:
        r, c = q.popleft()   # 현재 위치하는 좌표

        # (N, M)위치에 도달한 경우
        if r == N - 1 and c == M - 1:
            return maze[r][c]

        # 현재 좌표에서 동서남북 좌표를 탐색
        dr = [0, 0, 1, -1]   # 동서남북
        dc = [1, -1, 0, 0]    
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                maze[nr][nc] = maze[r][c] + 1
                q.append((nr, nc))


# 미로 생성하기
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# 최소 이동거리 출력
print(escape_maze(maze, N, M))



# 실행결과(메모리:32452KB, 시간:128ms)