import sys
sys.stdin = open("5_뒤집힌덧셈.txt")

X, Y = map(str, input().split())

RevX = int(X[::-1])
RevY = int(Y[::-1])

Rev_sum = int(str(RevX + RevY)[::-1])

print(Rev_sum)
