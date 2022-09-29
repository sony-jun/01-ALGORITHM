list_ = []
dict_ = dict() 

for _ in range(10):
    list_.append(int(input()))

mean1 = sum(list_) // len(list_)

for i in list_:
    if i in dict_:
        dict_[i] += 1

    else: 
        dict_[i] = 1

mean2 = max(dict_, key=dict_.get)

print(mean1)
print(mean2)