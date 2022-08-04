# 행렬의 크기 입력 받기
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 합을 구할 부분의 개수
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    cnt = 0
    # i-1부터 x까지, j-1부터 y까지 for문으로 구한 합
    for a in range(i-1, x):
        for b in range(j-1, y):
            cnt += matrix[a][b]

    print(cnt)