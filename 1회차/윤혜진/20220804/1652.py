# https://www.acmicpc.net/problem/1652
# 문제1652번.누울 자리를 찾아라
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 방의 크기 N
- 1 <= N <= 100
2. N줄에 N개의 문자
- .: 아무것도 없음
- X: 짐이 있는 곳
'''



# 출력
'''
1. 가로로 누울 수 있는 자리 갯수, 세로로 누울 수 있는 자리 갯수 출력
<누울 수 있는 자리 조건>
1. 똑바로 연속해서 2칸 이상의 빈 칸이 존재해야함
2. 가로로 누울 수도 있고, 세로로 누울 수도 있음
3. 누울 때는 반드시 벽이나 짐에 닿게 됨
'''



# 코드 1
import sys

sys.stdin = open('input_text/1652.txt')

# N x N 크기의 방 만들기
N = int(input())
room = [list(input()) for _ in range(N)]

# 각 행을 둘러보면서 빈 자리가 연속해서 두칸이 존재하면, 가로로 누울 수 있음
row_cnt = 0
for r in range(N):
    cnt = 0
    for c in range(N):
        if room[r][c] == '.':
            cnt += 1
        elif room[r][c] == 'X':
            if cnt >= 2:
                row_cnt += 1
                cnt = 0   # 초기화
            else:
                cnt = 0   # 초기화
    if cnt >= 2:
        row_cnt += 1

print(row_cnt, end=' ')

# 각 열을 둘러보면서 빈 자리가 연속해서 두칸이 존재하면, 세로로 누울 수 있음
col_cnt = 0
for c in range(N):
    cnt = 0
    for r in range(N):
        if room[r][c] == '.':
            cnt += 1
        elif room[r][c] == 'X':
            if cnt >= 2:
                col_cnt += 1
                cnt = 0   # 초기화
            else:
                cnt = 0   # 초기화
    if cnt >= 2:
        col_cnt += 1

print(col_cnt, end=' ')



# 실행결과(메모리:30840KB, 시간:84ms)



# 코드 2 - 위 코드 리팩토링(함수화)
import sys

sys.stdin = open('input_text/1652.txt')

# 각 줄을 둘러보면서 빈 자리가 연속해서 두칸이 존재하면 누울 수 있음
def check(room):
    tot_cnt = 0
    for row in room:
        cnt = 0
        for block in row:
            if block == '.':
                cnt += 1
            elif block == 'X':
                if cnt >= 2:
                    tot_cnt += 1
                    cnt = 0   # 초기화
                else:
                    cnt = 0   # 초기화
        if cnt >= 2:
            tot_cnt += 1
    
    return tot_cnt


# N x N 크기의 방 만들기
N = int(input())
room = [list(input()) for _ in range(N)]

# 가로로 누울 수 있는 자리 갯수
print(check(room), end=' ')

# 세로로 누울 수 있는 자리 갯수
new_room = list(zip(*room))
print(check(new_room), end=' ')



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 3
import sys

sys.stdin = open('input_text/1652.txt')

# N x N 크기의 방 만들기
N = int(input())
room = [input() for _ in range(N)]

# 각 행을 둘러보면서 빈 자리가 연속해서 두칸이 존재하면, 가로로 누울 수 있음
row_cnt = 0
for row in room:
    for section in row.split('X'):
        if len(section) >= 2:
            row_cnt += 1

print(row_cnt, end=' ')

# 행렬 위치를 바꾼 N x N 크기의 방 만들기
new_room = ['' * N for _ in range(N)]
for c in range(N):
    for r in range(N):
        new_room[c] += room[r][c]

# 각 열을 둘러보면서 빈 자리가 연속해서 두칸이 존재하면, 세로로 누울 수 있음
col_cnt = 0
for row in new_room:
    for section in row.split('X'):
        if len(section) >= 2:
            col_cnt += 1

print(col_cnt, end=' ')



# 실행결과(메모리:30840KB, 시간:72ms)