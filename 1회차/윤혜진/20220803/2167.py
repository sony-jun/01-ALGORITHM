# https://www.acmicpc.net/problem/2167
# 문제2167번.2차원 배열의 합
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 배열의 크기 N, M
- 1 <= N, M <= 300
2. N개의 줄에 M개의 정수
- -10,000 <= 정수 <= 10,000
3. 합을 구할 부분의 갯수 K
- 1 <= K <= 10,000
4. K개의 줄에 4개의 정수 i,j,x,y
- 1 <= i <= x <= N
- 1 <= j <= y <= M
'''



# 출력
'''
1. K개의 줄에 순서대로 배열의 합을 출력
- 2차원 배열에서 (i,j)위치부터 (x,y)위치까지 저장되어 있는 수들의 합
'''



# 코드 1
import sys

sys.stdin = open('input_text/2167.txt')

# 행렬 만들기
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# (i,j)위치부터 (x,y)위치까지 사각형 내 합 출력
K = int(input())
for _ in range(K):   # 총 계산 횟수
    i, j, x, y = map(lambda x: int(x) - 1, input().split())
    tot_sum = 0
    for r in range(i, x + 1):
        for c in range(j, y + 1):
            tot_sum += matrix[r][c]
   
    print(tot_sum)




# 실행결과(pypy3로 제출했을때, 메모리:118468KB, 시간:4184ms)



# 코드 2 - 누적합
import sys

sys.stdin = open('input_text/2167.txt')

# 행렬 만들기
N, M = map(int, input().split())
matrix = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 행렬을 가로로 누적합하기
acc_matrix = [[0] * (M + 1)] + [[0] * (M + 1) for _ in range(N)]
for r in range(N + 1):
    acc = 0
    for c in range(M + 1):
        acc += matrix[r][c]
        acc_matrix[r][c] = acc

# 가로로 누적합한 행렬을 세로로 누적합하기
for c in range(M + 1):
    acc = 0
    for r in range(N + 1):
        acc += acc_matrix[r][c]
        acc_matrix[r][c] = acc

# (i,j)위치부터 (x,y)위치까지 사각형 내 합 출력
K = int(input())
for _ in range(K):   # 총 계산 횟수
    i, j, x, y = map(int, input().split())
    tot_sum = acc_matrix[x][y] - acc_matrix[i-1][y] - acc_matrix[x][j-1] + acc_matrix[i-1][j-1]
    print(tot_sum)



# 실행결과(메모리:36484KB, 시간:1196ms)



# 코드 3 - 누적합
import sys
from itertools import accumulate

sys.stdin = open('input_text/2167.txt')

# 행렬 만들기
N, M = map(int, input().split())

# 행렬을 가로로 누적합하기
acc_matrix = [[0] + list(accumulate(map(int, input().split()))) for _ in range(N)]

# 가로로 누적합한 행렬을 세로로 누적합하기
acc_matrix = [[0] + list(accumulate(acc_row)) for acc_row in zip(*acc_matrix)]   # 행열이 뒤바뀜

# (i,j)위치부터 (x,y)위치까지 사각형 내 합 출력
K = int(input())
for _ in range(K):   # 총 계산 횟수
    i, j, x, y = map(int, input().split())
    tot_sum = acc_matrix[y][x] - acc_matrix[y][i-1] - acc_matrix[j-1][x] + acc_matrix[j-1][i-1]
    print(tot_sum)
   


# 실행결과(메모리:36352KB, 시간:1192ms)