
a, b = map(int, input().split())


min_ = min(a, b)
max_ = max(a, b)
for i in range(min_, 0, -1) :
    if max_ % i == 0 and min_ % i == 0 :
        print(i)
        break
for i in range(1, max_+1) :
    if i * min_ % max_ == 0:
        print(i*min_)
        break