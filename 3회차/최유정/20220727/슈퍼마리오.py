# https://www.acmicpc.net/problem/2851

list_ = []
p = 0
sum_ = 0

for i in range(10):
    list_.append(int(input()))
for l in range(len(list_)):
    sum_ += list_[l]
    if sum_ >= 100:
        s = sum(list_[:l])
        if 100-s > sum_-100:
            p = sum_
        elif 100-s < sum_-100:
            p = s
        elif 100-s == sum_-100:
            p = sum_
        print(p)
        # print(f'sum:{sum_} s:{s}' )
        break
