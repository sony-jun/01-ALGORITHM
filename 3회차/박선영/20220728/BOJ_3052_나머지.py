list_ = []
for i in range(10):
    list_.append(int(input()) % 42)
print(10 - (len(list_) - len(list(set(list_)))))