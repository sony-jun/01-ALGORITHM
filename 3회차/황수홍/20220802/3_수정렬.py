N = int(input())
list = []

for i in range(N):
    a = int(input())
    list.append(a)

list = sorted(list)

for j in range(len(list)):
    print(list[j])
