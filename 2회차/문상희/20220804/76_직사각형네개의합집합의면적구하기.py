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




# seet = []
# for _ in range(4):
#     line = list(map(int, input().split()))
#     seet.append(line)

# a1 = (seet[0][2] - seet[0][0]) * (seet[0][3] - seet[0][1])

# a2 = a1 + ((seet[1][2] - seet[1][0]) * (seet[1][3] - seet[1][1])) - ((seet[1][0] - seet[0][2]) * (seet[1][1] - seet[0][1]))
# # print(a1, a2)
# a3 = a2 + ((seet[2][2] - seet[2][0]) * (seet[2][3] - seet[2][1]))

# area = 0
# for i in range(4):
#     area += (seet[i][2] - seet[i][0]) * (seet[i][3] - seet[i][1])
#     for j in range(i):
#         if seet[j][2] - seet[i][0] > 0 and seet[j][3] - seet[i][1] > 0:
#             area -= ((seet[j][2] - seet[i][0]) * (seet[j][3] - seet[i][1]))
# print(area)


