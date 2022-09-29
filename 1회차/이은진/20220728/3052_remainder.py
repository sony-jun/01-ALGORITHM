in_list = []
for _ in range(10):
    in_list.append(int(input()))

my_dict = {}
for i in in_list:
    x = i % 42
    if x not in my_dict.keys():
        my_dict[x] = 1 
print(len(my_dict))