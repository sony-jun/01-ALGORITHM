new_num = []
for i in range(1, 1001):
    for j in range(i, 1001):
        new_num.append(j)
sort_ = sorted(new_num)
a, b = map(int, input().split())
print(sum(sort_[a-1:b]))