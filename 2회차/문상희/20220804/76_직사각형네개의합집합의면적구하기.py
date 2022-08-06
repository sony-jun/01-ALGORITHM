base = []
for i in range(101):
    base_line =[]
    for j in range(101):
        base_line += [0]
    base.append(base_line)

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            base[i][j] = 1
cnt = 0
for line in base:
    cnt += sum(line)
print(cnt)