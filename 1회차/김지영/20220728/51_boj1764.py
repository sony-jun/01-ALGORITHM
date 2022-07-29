n,m = map(int, input().split())
name_dict = {}
result_list = []
for i in range(n):
    name = input()
    name_dict[name] = 'not hear'
for i in range(m):
    name = input()
    if name in name_dict:
        result_list.append(name)
    else : name_dict[name] = 'not see'
result_list.sort()
print(len(result_list))
for i in result_list:
    print(i)