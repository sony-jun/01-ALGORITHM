numbers1 = []
for i in range(2):
    numbers1.append(list(map(int,input().split())))

numbers2 = []
for i in range(2):
    numbers2.append(list(map(int,input().split())))

result = []
for i in range(2):
    result.append([0 for i in range(3)])

for i in range(2):
    for j in range(3):
        result[i][j] = numbers1[i][j]*numbers2[i][j]

for res in result:
    print(*res,sep=' ')
