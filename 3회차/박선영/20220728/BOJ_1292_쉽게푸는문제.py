A, B = map(int, input().split())
data = [0]
for i in range(1, B):
    for j in range(i):
        data.append(i)

print(sum(data[A:B+1]))