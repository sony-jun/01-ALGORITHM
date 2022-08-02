# x, y = 456, 789

# x = list(str(x))[::-1]
# x = int(''.join(x))
# # print(x)

# y = list(str(y))[::-1]
# y = int(''.join(y))
# # print(y)

# sum = list(str(x + y))[::-1]
# sum = int(''.join(sum))
# print(sum)

## ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

x, y = map(int, input().split())
print(int(''.join(list(str(int(''.join(list(str(x))[::-1])) + int(''.join(list(str(y))[::-1]))))[::-1])))