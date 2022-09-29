a, b = map(int, input().split())
l = []

for i in range(1, 50):
    for j in range(i):
        l.append(i)

print(sum(l[a - 1:b]))

# n = 1
# while len(l) < b:
#     for _ in range(n):
#         l.append(n)
#     n+=1
