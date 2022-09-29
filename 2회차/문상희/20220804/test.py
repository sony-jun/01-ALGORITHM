seet1 = []
a = seet1.append(list(map(int, input().split())))
b = seet1.append(list(map(int, input().split())))

seet2 = []
a2 = seet2.append(list(map(int, input().split())))
b2 = seet2.append(list(map(int, input().split())))

for i in range(len(seet1)):
    for j in range(len(seet1[0])):
        print(seet1[i][j] * seet2[i][j], end = ' ')
    print()