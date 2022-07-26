my_dict = {}
for t in range(1, 6):
    my_dict[t] = sum(list(map(int, input().split())))
max_ = max(my_dict, key=my_dict.get)
print(f'{max_}, {my_dict[max_]}')