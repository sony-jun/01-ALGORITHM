# https://www.acmicpc.net/problem/4396
# 문제4396번.지뢰찾기
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. n X n 격자 크기
- 0 < n <= 10
2. n개의 줄에 n개 지뢰의 위치
- .: 지뢰가 없는 지점
- *: 지뢰가 있는 지점
3. 그 다음 n개의 줄에는 길이가 n인 문자열 입력
- x: 이미 열린 칸
- .: 아직 열리지 않은 칸
'''



# 출력
'''
1. 각각의 위치가 정확하게 채워진 판를 표현해 출력
- 지뢰가 없으면서 열린 칸: 0~8 사이의 숫자 (인접 8개 칸 중 지뢰의 갯수)
- 지뢰가 있는 칸이 열린 경우: 지뢰가 있는 모든 칸을 *로 표시
- 다른 모든 지점: .으로 표시
'''



# 코드 1
import sys

sys.stdin = open('input_text/4396.txt')

def cnt_bomb(r, c, grid, n):   # 주변 8칸에 1씩 증가
    # 순서대로 위왼, 위중앙, 위오른, 중앙왼, 중앙오른, 아래왼, 아래중앙, 아래오른
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]   
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == '.':
            continue
        else:
            grid[nr][nc] += 1


# 첫번째/두번째 그리드, 결과 그리드 만들기
n = int(input())
first = [list(input()) for _ in range(n)]
sec = [list(input()) for _ in range(n)]
rst = [[0] * n for _ in range(n)]   # 모든 칸 0으로 초기화

# 첫번째와 두번째 그리드를 비교하면서 결과 그리드에 값 넣기
bomb_locs = []   # 모든 지뢰 위치
bomb_open = False   # 지뢰가 있는 칸이 열렸는지 여부
for r in range(n):
    for c in range(n):
        # 지뢰가 없으면서 열린 칸
        if first[r][c] == '.' and sec[r][c] == 'x':
            continue
        # 지뢰가 없으면서 열지 않은 칸
        elif first[r][c] == '.' and sec[r][c] == '.':
            rst[r][c] = '.'
        # 지뢰가 있으면서 열지 않은 칸
        elif first[r][c] == '*' and sec[r][c] == '.':
            # 주변 8칸에 1씩 증가시킴
            cnt_bomb(r, c, rst, n)
            # 자신이 위치한 칸은 '.'으로 표시
            rst[r][c] = '.'
            # 지뢰 위치 기록
            bomb_locs.append((r, c))
        # 지뢰가 있으면서 열린 칸
        elif first[r][c] == '*' and sec[r][c] == 'x':
            bomb_open = True
            # 주변 8칸에 1씩 증가시킴
            cnt_bomb(r, c, rst, n)
            # 지뢰 위치 기록
            bomb_locs.append((r, c))

# 지뢰가 있는 칸이 열렸다면, 모든 지뢰 칸을 표시
if bomb_open:
    for r, c in bomb_locs:
        rst[r][c] = '*'

# rst 그리드 출력
for row in rst:
    print(''.join(map(str, row)))



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 2 - 위 코드 리팩토링
import sys

sys.stdin = open('input_text/4396.txt')

def cnt_bomb(r, c, grid, n):   # 주변 8칸에 1씩 증가
    # 순서대로 위왼, 위중앙, 위오른, 중앙왼, 중앙오른, 아래왼, 아래중앙, 아래오른
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]   
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == '.':
            continue
        else:
            grid[nr][nc] += 1


# 첫번째/두번째 그리드, 결과 그리드 만들기
n = int(input())
first = [list(input()) for _ in range(n)]
sec = [list(input()) for _ in range(n)]
rst = [[0] * n for _ in range(n)]   # 모든 칸 0으로 초기화

# 첫번째와 두번째 그리드를 비교하면서 결과 그리드에 값 넣기
bomb_locs = []   # 모든 지뢰 위치
bomb_open = False   # 지뢰가 있는 칸이 열렸는지 여부
for r in range(n):
    for c in range(n):
        # 지뢰가 있음
        if first[r][c] == '*':
            cnt_bomb(r, c, rst, n)   # 주변 8칸에 1씩 증가시킴
            bomb_locs.append((r, c))   # 지뢰 위치 기록
            # 열었음
            if sec[r][c] == 'x':
                bomb_open = True
            # 열지 않았음
            else:
                rst[r][c] = '.'   # 자신이 위치한 칸은 '.'으로 표시
        
        # 지뢰가 없음
        elif first[r][c] == '.':
            # 열지 않았음
            if sec[r][c] == '.':
                rst[r][c] = '.'

# 지뢰가 있는 칸이 열렸다면, 모든 지뢰 칸을 표시
if bomb_open:
    for r, c in bomb_locs:
        rst[r][c] = '*'

# rst 그리드 출력
for row in rst:
    print(''.join(map(str, row)))



# 실행결과(메모리:30840KB, 시간:68ms)