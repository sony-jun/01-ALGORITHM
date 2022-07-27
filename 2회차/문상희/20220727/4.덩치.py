n = int(input())
data = []
rank = []

for i in range(n):
    people = list(map(int, input().split()))
    data.append(people)

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count + 1)

for i in range(n):
    print(rank[i], end = ' ')