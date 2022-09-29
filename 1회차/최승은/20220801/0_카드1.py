n = int(input())

n_list = []
for i in range(1,n+1):
    n_list.append(i)
for i in range(n-1):
    print(n_list.pop(0))
    a = n_list.pop(0)
    n_list.append(a)
print(n_list.pop(0))
