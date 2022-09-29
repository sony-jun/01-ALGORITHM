a, b = map(int, input().split())

max_a = a // 2
max_b = b // 2
print(max_a if max_a < max_b else max_b)