import sys

sys.stdin = open("47_뒤집힌 덧셈.txt")
# 나의 방법
# a, b = map(int, input().split())

# c = str(a)[::-1]
# d = str(b)[::-1]
# e = int(c) + int(d)
# print(int(str(e)[::-1]))
# 다른사람 방법
def Rev(X):
    X = int(X[::-1])
    return X

X, Y = input().split(' ')
result = Rev(str(Rev(X) + Rev(Y)))
print(result)
