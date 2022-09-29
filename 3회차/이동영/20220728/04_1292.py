list_ = []
result = 0

for i in range(1,46):
    for j in range(1,i+1):
        list_.append(i)

m, n = map(int, input().split())

for i in range(min(m,n)-1,max(m,n)):
    result += list_[i]

print(result)