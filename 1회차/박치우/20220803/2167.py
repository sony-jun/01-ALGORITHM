import sys
input = sys.stdin.readline

H, W = map(int, input().split())
number = []
for _ in range(H):
    number.append(list(map(int, input().split())))

dp = [[0 for _ in range(W+1)] for _ in range(H+1)]


# [0][0]부터 [i][j]까지의 합을 저장해준다.
for i in range(1, H+1) :
    for j in range(1, W+1) :
        dp[i][j] = number[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]


# inclusive-exclusive방법을 사용해서 [i][j]부터 [x][y]까지의 합을 구해준다.
# [x][y]에서 [i-1][y], [x][j-1]을 빼주면 [i-1][j-1]부분의 뺼셈이 두번 이루어지므로 한번 더해줘서 보정해준다.
for t in range(int(input())):
    i, j, x, y = map(int, input().split())
    sum = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
    print(sum)


