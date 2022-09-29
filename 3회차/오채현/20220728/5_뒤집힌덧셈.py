x, y = input().split()

total = str(int(x[::-1]) + int(y[::-1]))

print(int(total[::-1]))

# def Rev(n):
#     return int(n[::-1])
# X_Y = str(Rev(X) + Rev(Y))
# print(Rev(X_Y))