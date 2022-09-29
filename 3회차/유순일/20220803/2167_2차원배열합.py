# 배열의 크기 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# N행까지, M개의 열이 있는 숫자 리스트 만들기.

# 부분의 개수 입력
K = int(input())        # K는 K개의 좌표 제시.
dp = [[0] * (M+1) for _ in range(N+1)]

# arr의 총합 구하기.
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# 좌표범위에서 합 구하기.
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
    
# https://velog.io/@norighthere/%EB%B0%B1%EC%A4%80-2167-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4%EC%9D%98-%ED%95%A9