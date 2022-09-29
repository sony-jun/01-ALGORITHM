# 평균값을 구해야하고 
# 최빈값을 구해야 한다

N = int(input())
lst_ = []
for i in range(N):
    lst_.append(int(input()))
print(int(sum(lst_)/10))

y = list(set(lst_))
set_ = []

for i in range(len(y)):
    set_.append(lst_.count(y[i]))
print(y[set_.index(max(set_))])