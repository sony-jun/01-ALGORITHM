N = int(input())

li = []

for _ in range(N):
    num = int(input())
    li.append(num)

print(*sorted(li), sep = '\n')