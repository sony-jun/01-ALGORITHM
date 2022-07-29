l = []

for i in range(1, 50):
    for j in range(i):
        l.append(i)

a, b = map(int, input().split())
print(sum(l[a - 1:b]))
