# https://www.acmicpc.net/problem/13567
# 문제13567번.로봇
# 시간제한:1초, 메모리제한:512MB



# 입력
'''
1. 정사각형 S의 한변 길이 M, 로봇이 수행할 명령어 n개
- 로봇의 처음 위치는 (0, 0)이고, 동쪽을 바라보고 있음
- 오른쪽 맨 위 좌표는 (M, M)
- 1 <= M <= 1,000
- 1 <= n <= 1,000
2. n개 줄에 명령어
- TURN + 0 또는 1
    - 0: 왼쪽으로 90도 회전
    - 1: 오른쪽으로 90도 회전
- MOVE + 이동거리
    - 0 < 이동거리 <= 1,000
- S의 바깥으로 완전히 나가게 된다면, 명령어는 유효하지 않음
- 일령의 명령어 열이 모두 유효하다면, 명령어 열은 유효함
'''



# 출력
'''
1. 명령어가 유효하다면 로봇의 x, y위치 출력, 유효하지 않다면 -1 출력
'''



# 코드 
import sys
from pprint import pprint

sys.stdin = open('input_text/13567.txt')

M, n = map(int, input().split())   # M: 정사각형S의 크기, n: 명령어 갯수
r, c = 0, 0   # 로봇의 시작 위치

# 시계방향 델타 값(동남서북)
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
idx = 0   # 가장 처음 (0,0) 좌표에선 동쪽을 바라봄

# 명령어에 따라 동작시킴
available = True   # 명령어 열이 유효한지 확인
for _ in range(n):
    cmd, num = input().split()
    
    # 방향전환 명령어
    if cmd == 'TURN':
        # 시계방향 회전(오른쪽으로 90도 회전)
        if num == '1':
            idx = (idx + 1) % 4
        # 반시계방향 회전(왼쪽으로 90도 회전)
        elif num == '0':
            # 현재 동쪽 방향을 보고 있는 경우
            if idx == 0:
                idx = 3
            else:
                idx -= 1
    
    # 이동 명령어
    elif cmd == 'MOVE':
        r += dr[idx] * int(num)
        c += dc[idx] * int(num)
        # 명령어에 따라 이동했을때, 범위를 벗어날 경우
        if not(0 <= r <= M and 0 <= c <= M):
            available = False
            break

# 명령어 열이 유효하면 로봇 위치 출력
if available:
    print(c, r)
else:
    print(-1)



# 실행결과(메모리:30840KB, 시간:72ms)