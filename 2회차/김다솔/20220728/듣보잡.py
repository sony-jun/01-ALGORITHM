n, m = list(map(int, input().split()))
dict_ = dict()

for i in range(n):
    p = input()
    dict_[p] = '듣도못한'
    
list_ = []
for i in range(m):
    p = input()
    if p in dict_:
        list_.append(p)
        
list_.sort()
for p in list_:
    print(p)
    