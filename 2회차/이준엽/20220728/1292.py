arr = []

for i in range(1,46):
    for j in range(i):
        arr.append(i)

a, b = map(int,input().split())
arr = arr[a-1:b]

print(sum(arr))