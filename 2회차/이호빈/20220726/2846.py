N = int(input())
up = list(map(int, input().split()))
size = []
result = 0
count = 0

for i in range(1, len(up)):
    if up[i] > up[i - 1]:
        result += up[i] - up[i - 1]
        size.append(result)
    else:
        result = 0
        size.append(result)

print(max(size)) 