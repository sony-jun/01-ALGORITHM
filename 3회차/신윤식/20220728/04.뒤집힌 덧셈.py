# https://www.acmicpc.net/problem/1357

X, Y = input().split()

def Rev(N):
    return int(N[::-1])

X_Y = str(Rev(X) + Rev(Y))
print(Rev(X_Y))