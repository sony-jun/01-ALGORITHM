# x, y = map(int, input().split())

# RevX = map(int, str(x))[::-1]
# RevY = map(int, str(y))[::-1]

# print(RevX+RevY)

# Alt 1 - jeong

# def reverse(x):
#     if type(x) == int:
#         x = list(str(x))[::-1]
#     return x

# def reverse(y):
#     y = y[::-1]
#     return y

# x,y = map(int, input().split())

# SumXY = sum(reverse(x),reverse(y))
# print(sum)

x, y = input().split()
rev = str(int(x[::-1]) + int(y[::-1]))
print(int(rev[::-1]))