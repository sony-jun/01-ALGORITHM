a, b = map(int, input().split())
print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))