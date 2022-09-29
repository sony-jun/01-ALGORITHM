T = int(input())
result = []

for i in range(T + 1):
    result.append(i)
print(*result[::-1])