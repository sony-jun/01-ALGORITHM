def Rev(X):
  X = int(X[::-1])
  return X

x, y = input().split()
print(Rev(str(Rev(x)+Rev(y))))