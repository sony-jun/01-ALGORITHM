N = int(input())

temp_list = []
name_list = []
dict = {}

for i in range(1, N+1):
    temp_list.append(input().split())

for i in temp_list:
    name_list.append(i[0])

for i in name_list :
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

sorted_keys_list = sorted(list(dict.keys()), reverse = True)

for k in sorted_keys_list:
    if dict.get(k) % 2 != 0:
        print(k)