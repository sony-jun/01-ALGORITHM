n = int(input())
max_lst = []
sum = 0
sum_lst = []
lst = list(map(int,input().split(' ')))
lst.append(0)
for i in range(n):
    if lst[int(i)] - lst[int(i) + 1] < 0:
        max_lst.append(abs(lst[int(i)] - lst[int(i) + 1]))
    else:
        max_lst.append(0)
for j in max_lst:
    if j != 0:
        sum += j
        sum_lst.append(sum)
    else :
        sum = 0
if max(sum_lst) > 1 :
    print(max(sum_lst))
else:
    print(0)


