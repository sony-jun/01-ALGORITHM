# https://www.acmicpc.net/problem/2592

list_ = []
dic_ = {}
for i in range(10):
    list_.append(int(input()))
avg_ = sum(list_)//10
print(avg_)

#최빈값
for j in list_:
    if j in dic_:
        dic_[j] += 1
    else:
        dic_[j] = 1
max_ = max(dic_.values())
for k, v in dic_.items():
    if v == max_:
        print(k)
