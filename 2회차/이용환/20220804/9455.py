import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N, M = map(int, input().rstrip().split())
    matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
    matrix_90 = []
    result = [0] * M
    for j in range(M):
        matrix_90x = []
        for k in range(N):
            matrix_90x.append(matrix[k][j])
        matrix_90.append(matrix_90x)# 세로를 가로로 바꾸기
    cnt = 0
    for r in range(M):
        res_matrix_90 = [i for i, ele in enumerate(matrix_90[r]) if ele == 1] # 각 행의 1이 들어있는 인덱스
        r_len = len(res_matrix_90) # 1이 들어있는 갯수
        max_res_r = 0 # 이동했을때 인덱스 합(최대값)
        for l in range(N-r_len, N):
            max_res_r += l # 이동했을때 인덱스
        cnt += max_res_r - sum(res_matrix_90) #인덱스 최대 값 - 현재 인덱스의 값
    print(cnt)