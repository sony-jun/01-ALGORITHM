N = int(input())

l = []
for i in range(N):
    l.append(tuple(map(int, input().split())))

result = []

for i in range(N):
    count = 1
    for j in range(N):
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            count += 1
    result.append(count)

for i in result:
    print(i, end=' ')