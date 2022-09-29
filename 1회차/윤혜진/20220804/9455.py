# https://www.acmicpc.net/problem/9455
# 문제9455번.박스
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트 케이스 T
2. m x n 크기의 그리드
- 1 <= m, n <= 100
3. 그리드의 각 행의 정보를 나타내는 n개의 정수
- 1: 박스가 들어있는 칸
- 0: 박스가 없는 칸
'''



# 출력
'''
1. 모든 박스를 바닥에 쌓일때까지 아래로 움직였을때, 모든 박스가 이동한 거리를 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/9455.txt')

T = int(input())

for _ in range(T):
    # 그리드 만들기
    m, n = map(int, input().split())
    grid = [input().split() for _ in range(m)]
    
    # 각 박스를 아래로 이동시키면서 이동거리 카운트
    tot_dis = 0
    for c in range(n):
        stack_height = 0   # 현재까지 쌓인 박스의 높이
        for r in range(m - 1, 0 - 1, -1):   # 행을 아래 -> 위 방향으로 탐색
            if grid[r][c] == '1':
                # 이동거리 = 현재 박스 높이 - 쌓인 박스 높이
                dis = (m - r - 1) - stack_height
                tot_dis += dis
                # 현재 박스 아래로 이동해 쌓기
                stack_height += 1
    
    print(tot_dis)
    


# 실행결과(메모리:30840KB, 시간:424ms)



# 코드 2
import sys

sys.stdin = open('input_text/9455.txt')

T = int(input())

for _ in range(T):
    # 그리드 만들기
    m, n = map(int, input().split())
    grid = [input().split() for _ in range(m)]
    
    # 각 박스를 아래로 이동시키면서 이동거리 카운트
    tot_dis = 0
    for c in range(n):
        cnt = 0   # 0의 갯수
        for r in range(m - 1, 0 - 1, -1):   # 행을 아래 -> 위 방향으로 탐색
            # 이동거리 = 아래의 0의 갯수
            if grid[r][c] == '1':
                tot_dis += cnt
            else:
                cnt += 1
    
    print(tot_dis)
    


# 실행결과(메모리:30840KB, 시간:388ms)