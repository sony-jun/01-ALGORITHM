x1_list = []
x2_list = []
y1_list = []
y2_list = []

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    x1_list.append(x1)
    x2_list.append(x2)
    y1_list.append(y1)
    y2_list.append(y2)

area = [[0] * (max(x2_list) - min(x1_list) + 1)
        for _ in range(min(y1_list), max(y2_list) + 2)]

for i in range(4):
    for j in range(y1_list[i], y2_list[i]):
        for k in range(x1_list[i], x2_list[i]):
            area[j - min(y1_list)][k - min(x1_list)] = 1

print(sum(map(sum, area)))
