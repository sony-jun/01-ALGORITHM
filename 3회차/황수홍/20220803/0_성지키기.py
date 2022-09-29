from sys import stdin

n, m = map(int,stdin.readline().split())
cas = []

for _ in range(n):
    cas.append(stdin.readline())

a, b = 0, 0

for i in range(n):
    if 'X' not in cas[i]:
        a += 1
for j in range(m):
    if 'X' not in [cas[i][j] for i in range(n)]:
        b += 1
print(max(a, b))