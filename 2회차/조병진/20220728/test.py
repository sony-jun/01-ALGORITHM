import sys

sys.stdin = open("input.txt")

# ------- 밑에 입력 --------

x, y = input().split()

x_rev = x[::-1]
y_rev = y[::-1]

sum_ = str(int(x_rev) + int(y_rev))
print(int(sum_[::-1]))
