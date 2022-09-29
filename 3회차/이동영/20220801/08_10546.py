n = int(input())
dict_ = dict()

for i in range(n+n-1):
    
    name = input()
    if name in dict_:
        dict_[name] += 1

    else :
        dict_[name] = 1

for k,v in dict_.items():
    if v % 2 != 0:
        print(k)    