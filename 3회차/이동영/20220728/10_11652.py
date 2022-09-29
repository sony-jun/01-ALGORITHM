from sys import stdin

N = int(stdin.readline())
numbers_list = []
max_list = []
dict_ = {}

for i in range(1,N+1):
    numbers_list.append( int(stdin.readline()))

for i in numbers_list:
    if i in dict_:
        dict_[i] += 1
    else:   
        dict_[i] = 1
max_ = dict_[max(dict_, key=dict_.get)]

for i in list(dict_.keys()):
    if dict_.get(i) == max_:
        max_list.append(i)

print(min(max_list))