arr = []
sum_ = 0

for i in range(10):
    arr.append(int(input()))

if 100 in arr:
    print('100')
else:
    for i in arr:
        sum_ += i
        if sum_ >= 100:
            if sum_ - 100 > 100 - (sum_ - i):
                sum_ -= i
                break

    print(sum_)
