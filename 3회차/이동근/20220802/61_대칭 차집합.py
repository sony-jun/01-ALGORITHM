a_len, b_len = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

# print(len((a | b) - (a & b)))
print((a_len + b_len) - 2 * len(a & b))