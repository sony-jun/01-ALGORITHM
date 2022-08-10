a, b = map(int, input().split())

a_row = a % 4 if a % 4 else 4
b_row = b % 4 if b % 4 else 4

a_col = a // 4 if a % 4 else a // 4 - 1
b_col = b // 4 if b % 4 else b // 4 - 1

row = abs(a_row - b_row)
col = abs(a_col - b_col)

print(row + col)

# 한 개씩 빼면 위와 같은 작업을 안해도 된다..
# a, b = map(int, input().split())
# a -= 1
# b -= 1
# print(abs(a//4-b//4)+abs(a % 4-b % 4))