max = 0
max_lst = []
lst = []

for i in range(5):
    lst.append(list(map(int,input().split())))
    max_lst.append(sum(lst[int(i)]))

for i in max_lst:
    if i > max:
        max = i

print(max_lst.index(max)+1, max)
