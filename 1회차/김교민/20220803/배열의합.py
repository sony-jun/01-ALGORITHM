import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

a = int(input())
board = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        board[i][j] = mat[i-1][j-1] + board[i][j-1] + board[i-1][j] - board[i-1][j-1]

for _ in range(a):
    n = []
    i, j, x, y = map(int, input().split())
    print(board[x][y] - board[x][j-1] - board[i-1][y] + board[i-1][j-1])