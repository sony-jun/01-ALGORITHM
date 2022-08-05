n = int(input())
list = []

for _ in range(1, n+1):
    number = int(input())
    list.append(number)
list_sort = sorted(list)
for i in range(len(list_sort)):
    print(list_sort[i])