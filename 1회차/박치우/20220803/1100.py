cs = [input() for i in range(8)]
count = 0
for i in range(len(cs)):
    for j in range(len(cs)):
        if i % 2 == 0 and j % 2 == 0 and cs[i][j] != '.':
            count +=1
        elif i % 2 == 1 and j % 2 ==1 and cs[i][j] != '.':
            count += 1
print(count)