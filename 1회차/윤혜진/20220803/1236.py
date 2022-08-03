# https://www.acmicpc.net/problem/1236
# 문제1236번.성 지키기
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 성의 세로 크기 N, 가로 크기 M
- 0 < N, M <= 50
2. N개의 줄에 성의 상태가 주어짐
- .: 빈칸
- X: 경비원이 있는 칸
'''



# 출력
'''
1. 모든 행과 모든 열에 한 명 이상의 경비원이 있어야 할때, 추가해야하는 경비원의 최솟값을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1236.txt')

# 행렬 생성
N, M = map(int, input().split())   
matrix = [list(input()) for _ in range(N)]

# 각 행을 둘러보면서 경비원이 없는 행 찾기
row_no_sec = []   # 경비원 없는 행
for r in range(N):
    for c in range(M):
        # 해당 행에 경비원이 있는 경우
        if matrix[r][c] == 'X':
            break
    # break없이 나왔다는 것은, 해당 행에 경비원이 없음을 의미
    else:
        row_no_sec.append(r)

# 각 열을 둘러보면서 경비원이 없는 열 찾기
col_no_sec = []   # 경비원이 없는 열
for c in range(M):
    for r in range(N):
        # 해당 열에 경비원이 있는 경우
        if matrix[r][c] == 'X':
            break
    # break없이 나왔다는 것은, 해당 열에 경비원이 없음을 의미
    else:
        col_no_sec.append(c)

# 추가해야하는 경비원의 최솟값
print(max(len(row_no_sec), len(col_no_sec)))



# 실행결과(메모리:30840KB, 시간:76ms)