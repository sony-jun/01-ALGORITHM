import sys
sys.stdin = open("47_뒤집힌 덧셈.txt", "r")

def Rev(X):
    return int(str(X)[::-1])

a, b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))
