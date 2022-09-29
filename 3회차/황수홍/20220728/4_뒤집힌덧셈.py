def Rev(X):
    a = int(X[::-1])
    return a

x, y = input().split()
print(Rev(str(Rev(x)+Rev(y))))