import sys
input = sys.stdin.readline
try:
    T = int(input())
    ball = [1, 2, 3]
    for i in range(T):
        X, Y = map(int, input().split())
        Xindex = ball.index(X)
        Yindex = ball.index(Y)
        ball[Xindex], ball[Yindex] = ball[Yindex], ball[Xindex]
    print(ball[0])
except ValueError:
    print(-1)