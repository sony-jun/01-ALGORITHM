t = int(input())
lst = []
for _ in range(t):
    body = kg, cm = list(map(int, input().split()))
    lst.append(body)

for i in lst:
    count = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count, end=' ')


