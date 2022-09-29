#2750



T = int(input())
n_list = []
for i in range(T):
    n_list.append(int(input()))

n_list.sort()
for i in range(len(n_list)):
    print(n_list[i])