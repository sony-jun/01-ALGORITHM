# https://www.acmicpc.net/problem/2615
# 문제2615번.오목
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 19개 각 줄마다 19개의 숫자가 표현됨
- 1: 검은 바둑알
- 2: 흰 바둑알
- 0: 알이 놓이지 않는 자리
'''



# 출력
'''
1. 검은색이 이겼을 경우엔 1, 흰색이 이겼을 경우엔 2, 아직 승부가 결정되지 않았을 경우엔 0을 출력
- 같은 색의 바둑알이 연속적(가로,세로,대각선)으로 5개가 놓이면, 그 색이 이기게 됨
- 6개 이상이 연속적으로 놓인 경우에는 이긴 것이 아님
2. 연속된 다섯 개의 바둑알 중에서 '가장 왼쪽'(또는 '가장 위쪽')에 있는 바둑알의 가로줄 번호와 세로줄 번호를 순서대로 출력
- 주의) 여섯 알 이상이 연속적으로 놓였다면, 이긴 것이 아님!!!!!!!!
'''



# 코드 1
import sys

sys.stdin = open('input_text/2615.txt')

# 해당 좌표에서부터 다섯 알이 연속적으로 놓였으면 True 반환 
def check_five(matrix, r, c, color):
    # 좌표값 따로 저장
    start_r = r   
    start_c = c  

    # 가로 확인
    dr = [0, 0]   # 좌, 우
    dc = [-1, 1]
    cnt = 1   # 연속한 동일 색의 바둑알 갯수
    for i in range(2):
        while True: 
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                cnt += 1
                r, c = nr, nc
            else:
                r, c = start_r, start_c
                break
    if cnt == 5:
        return (1, r, c)
    
    # 세로 확인
    dr = [-1, 1]   # 상, 하
    dc = [0, 0]
    cnt = 1   # 연속한 동일 색의 바둑알 갯수
    for i in range(2):
        while True: 
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                cnt += 1
                r, c = nr, nc
            else:
                r, c = start_r, start_c
                break
    if cnt == 5:
        return (1, r, c)

    # y = x 형태의 대각선 확인
    dr = [-1, 1]   # 1사분면 대각선, 3사분면 대각선
    dc = [1, -1]
    cnt = 1   # 연속한 동일 색의 바둑알 갯수
    for i in range(2):
        while True: 
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                cnt += 1
                r, c = nr, nc
            else:
                r, c = start_r, start_c
                break
    if cnt == 5:
        return (1, r + 4, c - 4)

    # y = -x 형태의 대각선 확인
    dr = [-1, 1]   # 2사분면 대각선, 4사분면 대각선
    dc = [-1, 1]
    cnt = 1   # 연속한 동일 색의 바둑알 갯수
    for i in range(2):
        while True: 
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                cnt += 1
                r, c = nr, nc
            else:
                r, c = start_r, start_c
                break
    if cnt == 5:
        return (1, r, c)

    # 가로, 세로, 대각선 모두 조건에 만족하지 않는 경우
    return (0, r, c)

# 오목판 만들기
matrix = [input().split() for _ in range(19)]

# 오목판의 각 좌표를 둘러보기
end = False
for r in range(0, 18 + 1):
    for c in range(0, 18 + 1):
        # 검은 바둑알
        if matrix[r][c] == '1':
            isfive, rst_r, rst_c = check_five(matrix, r, c, '1')
            if isfive:
                print(1)
                print(rst_r + 1, rst_c + 1)
                end = True
                break
        # 흰 바둑알
        elif matrix[r][c] == '2':
            isfive, rst_r, rst_c = check_five(matrix, r, c, '2')
            if isfive:
                print(2)
                print(rst_r + 1, rst_c + 1)
                end = True
                break    
    # 불필요한 반복 방지
    if end:
        break
else:    # break 없이 반복문이 끝난 경우, 아직 승부가 결정되지 않은 것임
    print(0)



# 실행결과(메모리:30840KB, 시간:80ms)



# 코드 2 - 위 풀이 리팩토링
import sys

sys.stdin = open('input_text/2615.txt')

# 해당 좌표에서부터 해당 벡터 방향으로 다섯 알이 연속적으로 놓였으면 True 반환 
def isfive(dr, dc, color, r, c) -> bool:
    global matrix
    
    start_r, start_c = r, c   # 좌표값 따로 저장
    cnt = 1   # 연속한 동일 색의 바둑알 갯수
    for i in range(2):
        while True: 
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == color:
                cnt += 1
                r, c = nr, nc
            else:
                r, c = start_r, start_c
                break
    if cnt == 5:
        return True

    return False


# 해당 좌표에서 가로, 세로, 대각선 방향으로 다섯 알이 연속적으로 놓였는지 확인
def check_five(r, c, color): 
    # 가로 확인
    dr = [0, 0]   # 좌, 우
    dc = [-1, 1]
    if isfive(dr, dc, color, r, c):
        return (1, r, c)
    
    # 세로 확인
    dr = [-1, 1]   # 상, 하
    dc = [0, 0]
    if isfive(dr, dc, color, r, c):
        return (1, r, c)

    # y = x 형태의 대각선 확인
    dr = [-1, 1]   # 1사분면 대각선, 3사분면 대각선
    dc = [1, -1]
    if isfive(dr, dc, color, r, c):
        return (1, r + 4, c - 4)

    # y = -x 형태의 대각선 확인
    dr = [-1, 1]   # 2사분면 대각선, 4사분면 대각선
    dc = [-1, 1]
    if isfive(dr, dc, color, r, c):
        return (1, r, c)

    # 가로, 세로, 대각선 모두 조건에 만족하지 않는 경우
    return (0, r, c)


# 오목판 만들기
matrix = [input().split() for _ in range(19)]

# 오목판의 각 좌표를 둘러보기
end = False
for r in range(0, 18 + 1):
    for c in range(0, 18 + 1):
        # 검은 바둑알
        if matrix[r][c] == '1':
            five, rst_r, rst_c = check_five(r, c, '1')
            if five:
                print(1)
                print(rst_r + 1, rst_c + 1)
                end = True
                break
        # 흰 바둑알
        elif matrix[r][c] == '2':
            five, rst_r, rst_c = check_five(r, c, '2')
            if five:
                print(2)
                print(rst_r + 1, rst_c + 1)
                end = True
                break    
    # 불필요한 반복 방지
    if end:
        break
else:    # break 없이 반복문이 끝난 경우, 아직 승부가 결정되지 않은 것임
    print(0)



# 실행결과(메모리:30840KB, 시간:76ms)



# 코드 3
import sys

sys.stdin = open('input_text/2615.txt')

# 오목판 만들기
matrix = [input().split() for _ in range(19)]

# 오목판의 각 좌표를 둘러보기
answer = 0   # 무승부로 초기값 설정
for r in range(0, 18 + 1):
    for c in range(0, 18 + 1):
        if matrix[r][c] != '0':   # 바둑알(검은 바둑알, 흰 바둑알)이 있는 경우
            # 델타 탐색(오른쪽, 아래, 우하향, 우상향 - 가장 왼쪽 또는 위에 있는 좌표를 출력해야하므로)
            dr = [0, 1, 1, -1]
            dc = [1, 0, 1, 1]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                cnt = 1
                while True:
                    if 0 <= nr < 19 and 0 <= nc < 19 and matrix[nr][nc] == matrix[r][c]:
                        cnt += 1
                        nr += dr[i]
                        nc += dc[i]
                    else:
                        break
                if cnt == 5:
                    # 이전 좌표 위치
                    prev_r = r - dr[i]
                    prev_c = c - dc[i]
                    # 6목인지 확인
                    if not (0 <= prev_r < 19 and 0 <= prev_c < 19) or matrix[prev_r][prev_c] != matrix[r][c]:
                        answer = 1
                        print(matrix[r][c])
                        print(r + 1, c + 1)
                        break
            # 불필요한 반복 방지
            if answer:
                break
    # 불필요한 반복 방지
    if answer:
        break

if not answer:
    print(0)



# 실행결과(메모리:30840KB, 시간:76ms)